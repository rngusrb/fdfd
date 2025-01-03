import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from cepstrum import compute_human_cepstrum
from quantitative_eval import (
    compute_mean_std,
    compute_correlation,
    compute_distances,
    perform_t_test,
)

A = 0
E = 1
I = 2
O = 3
U = 4
MALE = 0
FEMALE = 0
FS = 16000
BY_GENDER = 5


def plot_signal_and_cepstrum(signal, cepstrum, fs, title):
    time = np.arange(len(signal)) / fs
    quefrency = np.arange(len(cepstrum)) / fs

    plt.figure(figsize=(12, 6))

    # Plot the time-domain signal
    plt.subplot(2, 1, 1)
    plt.plot(time, signal)
    plt.title(f"Time-Domain Signal - {title}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    # Plot the cepstrum
    plt.subplot(2, 1, 2)
    plt.plot(quefrency, cepstrum)
    plt.title(f"Cepstrum - {title}")
    plt.xlabel("Quefrency (s)")
    plt.ylabel("Amplitude")

    plt.tight_layout()
    plt.show()


def get_mean():
    mean_male = []
    mean_female = []
    for n in ("a", "e", "i", "o", "u"):
        for gender in ("male", "female"):
            fs1, a1 = wavfile.read(
                "./normalized_data/" + gender + "/" + gender + "_0_" + n + ".wav"
            )
            full_data = [0 for i in range(len(a1))]
            for i in ("0", "1", "2", "3", "4"):
                name = (
                    "./normalized_data/"
                    + gender
                    + "/"
                    + gender
                    + "_"
                    + i
                    + "_"
                    + n
                    + ".wav"
                )
                fs1, a2 = wavfile.read(name)
                for i in range(len(a1)):
                    full_data[i] += a2[i]
            for i in range(len(a1)):
                full_data[i] = full_data[i] / 5
            if gender == "male":
                mean_male.append(compute_human_cepstrum(full_data)[1])
            else:
                mean_female.append(compute_human_cepstrum(full_data)[1])

    return mean_male, mean_female


def compare_two_cepstrum(cepstrum1, cepstrum2, standard, idx):
    FS = 16000  # 샘플링 레이트를 가정합니다.
    quefrency1 = idx
    quefrency2 = idx

    if standard == A:
        title1 = "male_a"
        title2 = "female_a"
    elif standard == E:
        title1 = "male_e"
        title2 = "female_e"
    elif standard == I:
        title1 = "male_i"
        title2 = "female_i"
    elif standard == O:
        title1 = "male_o"
        title2 = "female_o"
    elif standard == U:
        title1 = "male_u"
        title2 = "female_u"

    row_labels = ["male", "female"]
    column_labels = [
        "Cepstral Peak quefrency",
        "Mean / Standard",
        "Correlation",
        "Distances",
        "T-Test",
    ]
    cell_text = [
        [
            quefrency1[np.argmax(cepstrum1)],
            compute_mean_std(cepstrum1),
            compute_correlation(cepstrum1, cepstrum2),
            compute_distances(cepstrum1, cepstrum2),
            perform_t_test(cepstrum1, cepstrum2),
        ],
        [
            quefrency2[np.argmax(cepstrum2)],
            compute_mean_std(cepstrum2),
            compute_correlation(cepstrum1, cepstrum2),
            compute_distances(cepstrum1, cepstrum2),
            perform_t_test(cepstrum1, cepstrum2),
        ],
    ]
    # 전체 그림 및 서브플롯 설정
    fig = plt.figure(figsize=(12, 10))

    # 첫 번째 켑스트럼 플롯
    ax1 = fig.add_subplot(4, 1, 1)
    ax1.plot(quefrency1, cepstrum1)
    ax1.set_title(f"Cepstrum - {title1}")
    ax1.set_xlabel("Quefrency (s)")
    ax1.set_ylabel("Amplitude")

    # 두 번째 켑스트럼 플롯
    ax2 = fig.add_subplot(4, 1, 2)
    ax2.plot(quefrency2, cepstrum2)
    ax2.set_title(f"Cepstrum - {title2}")
    ax2.set_xlabel("Quefrency (s)")
    ax2.set_ylabel("Amplitude")

    # 테이블 추가
    ax3 = fig.add_subplot(4, 1, 3)
    ax3.axis("off")  # 테이블에는 축이 필요 없으므로 숨깁니다.
    table = ax3.table(
        cellText=cell_text,
        rowLabels=row_labels,
        colLabels=column_labels,
        loc="center",
        cellLoc="center",  # 셀 내부 글자 정렬
        fontsize=10,  # 글자 크기 조정
    )
    table.scale(1, 2)  # 테이블 크기 조정 (폭, 높이)

    plt.tight_layout()
    plt.show()


def compare_two_mean_cepstrum(cepstrum1, cepstrum2, standard, idx):
    FS = 16000  # 샘플링 레이트를 가정합니다.
    quefrency1 = idx
    quefrency2 = idx

    if standard == A:
        title1 = "mean_male_a"
        title2 = "mean_female_a"
    elif standard == E:
        title1 = "mean_male_e"
        title2 = "mean_female_e"
    elif standard == I:
        title1 = "mean_male_i"
        title2 = "mean_female_i"
    elif standard == O:
        title1 = "mean_male_o"
        title2 = "mean_female_o"
    elif standard == U:
        title1 = "mean_male_u"
        title2 = "mean_female_u"

    row_labels = ["male", "female"]
    column_labels = [
        "Cepstral Peak quefrency",
        "Mean / Standard",
        "Correlation",
        "Distances",
        "T-Test",
    ]
    cell_text = [
        [
            quefrency1[np.argmax(cepstrum1)],
            compute_mean_std(cepstrum1),
            compute_correlation(cepstrum1, cepstrum2),
            compute_distances(cepstrum1, cepstrum2),
            perform_t_test(cepstrum1, cepstrum2),
        ],
        [
            quefrency2[np.argmax(cepstrum2)],
            compute_mean_std(cepstrum2),
            compute_correlation(cepstrum1, cepstrum2),
            compute_distances(cepstrum1, cepstrum2),
            perform_t_test(cepstrum1, cepstrum2),
        ],
    ]
    # 전체 그림 및 서브플롯 설정
    fig = plt.figure(figsize=(12, 10))

    # 첫 번째 켑스트럼 플롯

    ax1 = fig.add_subplot(4, 1, 1)
    ax1.plot(quefrency1, cepstrum1)
    ax1.set_title(f"Cepstrum - {title1}")
    ax1.set_xlabel("Quefrency (s)")
    ax1.set_ylabel("Amplitude")

    # 두 번째 켑스트럼 플롯
    ax2 = fig.add_subplot(4, 1, 2)
    ax2.plot(quefrency2, cepstrum2)
    ax2.set_title(f"Cepstrum - {title2}")
    ax2.set_xlabel("Quefrency (s)")
    ax2.set_ylabel("Amplitude")

    # 테이블 추가
    ax3 = fig.add_subplot(4, 1, 3)
    ax3.axis("off")  # 테이블에는 축이 필요 없으므로 숨깁니다.
    table = ax3.table(
        cellText=cell_text,
        rowLabels=row_labels,
        colLabels=column_labels,
        loc="center",
        cellLoc="center",  # 셀 내부 글자 정렬
        fontsize=10,  # 글자 크기 조정
    )
    table.scale(1, 2)  # 테이블 크기 조정 (폭, 높이)

    plt.tight_layout()
    plt.show()


def compare_all_cepstrum(
    cepstrum1, cepstrum2, cepstrum3, cepstrum4, cepstrum5, idx, que
):
    FS = 16000  # 샘플링 레이트를 가정합니다.
    aa = ["male", "female"]

    quefrency1 = que
    quefrency2 = que
    quefrency3 = que
    quefrency4 = que
    quefrency5 = que

    fig = plt.figure(figsize=(8, 8))

    # 첫 번째 켑스트럼 플롯
    ax1 = fig.add_subplot(5, 1, 1)
    ax1.plot(quefrency1, cepstrum1)
    ax1.set_title(aa[idx] + " a")
    ax1.set_xlabel("Quefrency (s)")
    ax1.set_ylabel("Amplitude")

    # 두 번째 켑스트럼 플롯
    ax2 = fig.add_subplot(5, 1, 2)
    ax2.plot(quefrency2, cepstrum2)
    ax2.set_title(aa[idx] + " e")
    ax2.set_xlabel("Quefrency (s)")
    ax2.set_ylabel("Amplitude")

    ax3 = fig.add_subplot(5, 1, 3)
    ax3.plot(quefrency3, cepstrum3)
    ax3.set_title(aa[idx] + " i")
    ax3.set_xlabel("Quefrency (s)")
    ax3.set_ylabel("Amplitude")

    ax4 = fig.add_subplot(5, 1, 4)
    ax4.plot(quefrency4, cepstrum4)
    ax4.set_title(aa[idx] + " o")
    ax4.set_xlabel("Quefrency (s)")
    ax4.set_ylabel("Amplitude")

    ax5 = fig.add_subplot(5, 1, 5)
    ax5.plot(quefrency5, cepstrum5)
    ax5.set_title(aa[idx] + " u")
    ax5.set_xlabel("Quefrency (s)")
    ax5.set_ylabel("Amplitude")
    a1 = 1 / quefrency2[np.argmax(cepstrum1)]
    a2 = 1 / quefrency2[np.argmax(cepstrum2)]
    a3 = 1 / quefrency2[np.argmax(cepstrum3)]
    a4 = 1 / quefrency2[np.argmax(cepstrum4)]
    a5 = 1 / quefrency2[np.argmax(cepstrum5)]

    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)
    print("\n")

    plt.tight_layout()
    plt.show()


def compare_all_cepstrum_v2(
    cepstrum1, cepstrum2, cepstrum3, cepstrum4, cepstrum5, que, idx, word
):
    FS = 16000  # 샘플링 레이트를 가정합니다.
    aa = ["male", "female"]

    quefrency1 = que
    quefrency2 = que
    quefrency3 = que
    quefrency4 = que
    quefrency5 = que

    fig = plt.figure(figsize=(8, 8))

    # 첫 번째 켑스트럼 플롯
    ax1 = fig.add_subplot(5, 1, 1)
    ax1.plot(quefrency1, cepstrum1)
    ax1.set_title(aa[idx] + "_0_" + word)
    ax1.set_xlabel("Quefrency (s)")
    ax1.set_ylabel("Amplitude")

    # 두 번째 켑스트럼 플롯
    ax2 = fig.add_subplot(5, 1, 2)
    ax2.plot(quefrency2, cepstrum2)
    ax2.set_title(aa[idx] + "_1_" + word)
    ax2.set_xlabel("Quefrency (s)")
    ax2.set_ylabel("Amplitude")

    ax3 = fig.add_subplot(5, 1, 3)
    ax3.plot(quefrency3, cepstrum3)
    ax3.set_title(aa[idx] + "_2_" + word)
    ax3.set_xlabel("Quefrency (s)")
    ax3.set_ylabel("Amplitude")

    ax4 = fig.add_subplot(5, 1, 4)
    ax4.plot(quefrency4, cepstrum4)
    ax4.set_title(aa[idx] + "_3_" + word)
    ax4.set_xlabel("Quefrency (s)")
    ax4.set_ylabel("Amplitude")

    ax5 = fig.add_subplot(5, 1, 5)
    ax5.plot(quefrency5, cepstrum5)
    ax5.set_title(aa[idx] + "_4_" + word)
    ax5.set_xlabel("Quefrency (s)")
    ax5.set_ylabel("Amplitude")

    a1 = 1 / quefrency2[np.argmax(cepstrum1)]
    a2 = 1 / quefrency2[np.argmax(cepstrum2)]
    a3 = 1 / quefrency2[np.argmax(cepstrum3)]
    a4 = 1 / quefrency2[np.argmax(cepstrum4)]
    a5 = 1 / quefrency2[np.argmax(cepstrum5)]

    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)
    print((a1 + a2 + a3 + a4 + a5) / 5)
    print("\n")
    plt.tight_layout()
    plt.show()


def get_cepstrum_arrays():
    male_cepstrums, female_cepstrums = [], []
    for gender in ("male", "female"):
        for i in ("a", "e", "i", "o", "u"):
            name = "./normalized_data/" + gender + "/" + gender + "_4_" + i + ".wav"
            fs1, data = wavfile.read(name)
            if gender == "male":
                male_cepstrums.append(compute_human_cepstrum(data)[1])
            else:
                female_cepstrums.append(compute_human_cepstrum(data)[1])
    return (
        male_cepstrums,
        female_cepstrums,
    )
