# CEPSTRUM ANALYSIS

## Data Normalization
![image](https://github.com/user-attachments/assets/aab5de2d-5903-499a-ad3c-228d65d93d14)
### 대역 통과 필터 적용
![image](https://github.com/user-attachments/assets/b4364824-3805-42d4-9cb8-938a2bb90d1e)


## CEPSTRUM


   def compute_cepstrum(signal):
       spectrum = fft(signal)
       epsilon = 1e-8
       log_amplitude = np.log(np.absolute(spectrum + epsilon))
       cepstrum = np.abs(ifft(log_amplitude))
       return cepstrum




## 결과
![image](https://github.com/user-attachments/assets/ea66b518-22d6-44d2-a4ca-f3cd0d2559ee)
