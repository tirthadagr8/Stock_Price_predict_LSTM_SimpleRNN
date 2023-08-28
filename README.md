# Stock_Price_predict_LSTM_SimpleRNN

This machine learning model is based on  Long Short Term Memory, a subset of Recurrent Neural Network. Two model, namely SimpleRNN and LSTM, are used separately. The data is scraped from Wall Street Journal. The data is first pre- processed, that is converted the values to range of 0 and 1 using MinMaxScaler and stored into 1 D array. The time step is based on time interval of the data. The training and test data is split. Then, various LSTM and SimpleRNN layers are added and trained
to see the accuracy in a graphical representation.
