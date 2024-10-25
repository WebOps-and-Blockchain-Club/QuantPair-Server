import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential #type:ignore
from tensorflow.keras.layers import Dense, LSTM, Input, Dropout#type:ignore
from sklearn.metrics import mean_squared_error, accuracy_score
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint#type:ignore
from tensorflow.keras.models import load_model#type:ignore
import yfinance as yf
import math

import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import requests

@api_view(['POST'])
@permission_classes([])
def showPredictedOutput(request) :
    if request.method == "POST" :
        fields = request.data

        stk1_ticker = fields['stk1']
        stk2_ticker = fields['stk2']

        stock1_df = yf.download(stk1_ticker)
        stock2_df = yf.download(stk2_ticker)

        stock1_adj_close = stock1_df[['Adj Close']].rename(columns={'Adj Close': 'Adj Close_Stock1'})
        stock2_adj_close = stock2_df[['Adj Close']].rename(columns={'Adj Close': 'Adj Close_Stock2'})

        combined_df = pd.concat([stock1_adj_close, stock2_adj_close], axis=1)

        window_size = 220

        combined_df['Stock1_MA'] = combined_df['Adj Close_Stock1'].rolling(window=window_size).mean()
        combined_df['Stock2_MA'] = combined_df['Adj Close_Stock2'].rolling(window=window_size).mean()

        plt.figure(figsize=(14, 7))
        plt.plot(combined_df['Adj Close_Stock1'], label='Pepsi', alpha=0.5)
        plt.plot(combined_df['Stock1_MA'], label='Pepsi Moving Average', color='red')
        plt.plot(combined_df['Adj Close_Stock2'], label='Coca-Cola', alpha=0.5)
        plt.plot(combined_df['Stock2_MA'], label='Coca-Cola Moving Average', color='blue')
        plt.title('Stock Prices with Moving Average Smoothing')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

        data = combined_df[['Stock1_MA', 'Stock2_MA']].dropna().values

        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(data)

        def create_buy_sell_labels(data, seq_size=5, future_step=1):
            X, Y = [], []
            for i in range(len(data) - seq_size - future_step):
                X.append(data[i:i + seq_size])  # Sequence of both stocks
                stock1_label = 1 if data[i + seq_size + future_step, 0] > data[i + seq_size, 0] else 0
                stock2_label = 1 if data[i + seq_size + future_step, 1] > data[i + seq_size, 1] else 0
                Y.append([stock1_label, stock2_label])  # Buy/sell labels for both stocks
            return np.array(X), np.array(Y)

        seq_size = 10
        future_step = 1
        x, y = create_buy_sell_labels(scaled_data, seq_size, future_step)

        train_size = int(len(x) * 0.8)
        x_train, x_test = x[:train_size], x[train_size:]
        y_train, y_test = y[:train_size], y[train_size:]

        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], x_train.shape[2]))
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], x_test.shape[2]))

        model = Sequential()
        model.add(Input(shape=(seq_size, 2)))
        model.add(LSTM(128, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(64, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(32, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(16, return_sequences=False))
        model.add(Dropout(0.2))
        model.add(Dense(2, activation='sigmoid'))

        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.summary()

        model_checkpoint = ModelCheckpoint('best_model.keras', monitor='val_accuracy', save_best_only=True, mode='max', verbose=1)

        model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=100, batch_size=32, verbose=2, callbacks=[model_checkpoint])

        best_model = load_model('best_model.keras')

        predictions_best = best_model.predict(x_test)

        buy_sell_signals_best = (predictions_best > 0.5).astype(int)

        accuracy_best = accuracy_score(y_test.flatten(), buy_sell_signals_best.flatten())
        resp1 = "Sell"
        resp2 = "Sell"

        if last_signal_best[0] == 1 :
            resp1 = "Buy"
        if last_signal_best[1] == 1 :
            resp2 = 'Buy'
        retDict = {
            'Stock 1' : resp1,
            'Stock 2' : resp2,
        }
        print(f"Accuracy on test data with the best model: {accuracy_best * 100:.2f}%")

        last_signal_best = buy_sell_signals_best[-1]

        print(f"Best Model - Stock 1: {'Buy' if last_signal_best[0] == 1 else 'Sell'}, Stock 2: {'Buy' if last_signal_best[1] == 1 else 'Sell'}")
        
        trainPredict_best = best_model.predict(x_train)
        trainScore_best = math.sqrt(mean_squared_error(y_train.flatten(), trainPredict_best.flatten()))
        testScore_best = math.sqrt(mean_squared_error(y_test.flatten(), predictions_best.flatten()))
        print(f'Best Model - Train Score: {trainScore_best:.2f} RMSE')
        print(f'Best Model - Test Score: {testScore_best:.2f} RMSE')
        return Response(retDict, status=status.HTTP_200_OK)

    return Response({'message' : 'Bad gateway'}, status=status.HTTP_400_BAD_REQUEST)