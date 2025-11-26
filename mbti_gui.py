import tkinter as tk
from tkinter import messagebox

class MBTIGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python MBTI Tester")
        self.root.geometry("600x450")  # 창 크기 설정
        self.root.resizable(False, False)

        # 데이터 초기화
        self.scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
        self.current_index = 0
        
        # 질문 리스트 (12문항)
        self.questions = [
            {"q": "주말에 자유 시간이 생겼을 때 나는?", "A": "친구들을 만나 활동적인 시간을 보낸다.", "B": "집에서 혼자만의 취미를 즐기며 쉰다.", "A_type": "E", "B_type": "I"},
            {"q": "새로운 사람들을 만나는 자리에서 나는?", "A": "먼저 말을 걸고 분위기를 주도한다.", "B": "주로 듣는 편이며, 누가 말을 걸어주길 기다린다.", "A_type": "E", "B_type": "I"},
            {"q": "생각을 정리할 때 나는?", "A": "말하면서 생각하는 편이다.", "B": "속으로 깊이 생각한 후 말하는 편이다.", "A_type": "E", "B_type": "I"},
            {"q": "영화를 볼 때 더 집중하는 것은?", "A": "현실적인 스토리와 디테일한 연출", "B": "영화가 담고 있는 의미와 상징적 메시지", "A_type": "S", "B_type": "N"},
            {"q": "일하는 방식에 있어 나는?", "A": "검증된 방식과 경험을 신뢰한다.", "B": "새롭고 독창적인 방법을 시도하는 것을 좋아한다.", "A_type": "S", "B_type": "N"},
            {"q": "숲을 볼 때 나는?", "A": "나무, 흙, 풀 냄새 등 구체적인 감각에 집중한다.", "B": "숲의 전체적인 분위기와 느낌을 상상한다.", "A_type": "S", "B_type": "N"},
            {"q": "친구가 고민을 털어놓을 때 나의 반응은?", "A": "문제 해결을 위한 현실적인 조언을 해준다.", "B": "친구의 감정에 공감하고 위로해준다.", "A_type": "T", "B_type": "F"},
            {"q": "의사결정을 할 때 더 중요한 것은?", "A": "논리적인 인과관계와 객관적 사실", "B": "나와 타인의 감정 및 관계에 미칠 영향", "A_type": "T", "B_type": "F"},
            {"q": "누군가 나를 비판했을 때 나는?", "A": "비판의 내용이 사실인지 논리적으로 따져본다.", "B": "기분이 상하고 마음에 오래 남는다.", "A_type": "T", "B_type": "F"},
            {"q": "여행을 갈 때 나는?", "A": "숙소, 맛집, 동선을 미리 계획하고 예약한다.", "B": "큰 틀만 잡고 현지 기분에 따라 움직인다.", "A_type": "J", "B_type": "P"},
            {"q": "책상이나 방의 상태는?", "A": "물건이 제자리에 정리정돈되어 있다.", "B": "필요한 물건이 어디 있는지만 알면 된다(다소 혼란).", "A_type": "J", "B_type": "P"},
            {"q": "마감 기한이 있는 일을 할 때 나는?", "A": "미리미리 계획을 세워 여유 있게 끝낸다.", "B": "임박해서 몰입하여 한 번에 처리한다.", "A_type": "J", "B_type": "P"},
        ]

        # 결과 해설 딕셔너리
        self.results_desc = {
            "ISTJ": "청렴결백한 논리주의자\n책임감이 강하고 현실적이며 매사에 철저합니다.",
            "ISFJ": "용감한 수호자\n차분하고 헌신적이며 타인의 감정을 잘 살핍니다.",
            "INFJ": "선의의 옹호자\n통찰력이 뛰어나고 공동체의 이익을 중요시합니다.",
            "INTJ": "용의주도한 전략가\n상상력이 풍부하고 계획적이며 완벽을 추구합니다.",
            "ISTP": "만능 재주꾼\n과묵하지만 관찰력이 뛰어나고 도구 사용에 능합니다.",
            "ISFP": "호기심 많은 예술가\n온화하고 겸손하며 삶의 여유를 즐깁니다.",
            "INFP": "열정적인 중재자\n상냥하고 이타적이며 낭만적인 이상을 추구합니다.",
            "INTP": "논리적인 사색가\n지적 호기심이 많고 끊임없이 탐구합니다.",
            "ESTP": "모험을 즐기는 사업가\n에너지가 넘치고 직관적이며 적응력이 뛰어납니다.",
            "ESFP": "자유로운 영혼의 연예인\n사교적이고 낙천적이며 분위기 메이커입니다.",
            "ENFP": "재기발랄한 활동가\n열정적이고 창의적이며 사람들과 어울리기를 좋아합니다.",
            "ENTP": "뜨거운 논쟁을 즐기는 변론가\n박학다식하고 독창적이며 끊임없이 도전합니다.",
            "ESTJ": "엄격한 관리자\n사물과 사람을 관리하는 데 뛰어난 실력을 갖췄습니다.",
            "ESFJ": "사교적인 외교관\n타인에게 세심하며 인기가 많고 돕는 것을 즐깁니다.",
            "ENFJ": "정의로운 사회운동가\n카리스마와 충만함으로 청중을 압도하는 리더입니다.",
            "ENTJ": "대담한 통솔자\n철저한 준비와 결단력으로 목표를 달성하는 리더입니다."
        }

        # UI 요소 생성
        self.create_widgets()

    def create_widgets(self):
        # 상단 진행 상황
        self.progress_label = tk.Label(self.root, text="", font=("Arial", 12), fg="gray")
        self.progress_label.pack(pady=10)

        # 질문 텍스트
        self.question_label = tk.Label(self.root, text="질문이 여기에 표시됩니다.", font=("Arial", 16, "bold"), wraplength=500, justify="center")
        self.question_label.pack(pady=30)

        # 버튼 프레임
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        # 선택 버튼 A
        self.btn_a = tk.Button(button_frame, text="A 선택", width=50, height=3, bg="#e1f5fe", command=lambda: self.process_answer("A"))
        self.btn_a.pack(pady=10)

        # 선택 버튼 B
        self.btn_b = tk.Button(button_frame, text="B 선택", width=50, height=3, bg="#fff3e0", command=lambda: self.process_answer("B"))
        self.btn_b.pack(pady=10)

        # 초기 질문 로드
        self.update_question()

    def update_question(self):
        if self.current_index < len(self.questions):
            q_data = self.questions[self.current_index]
            self.progress_label.config(text=f"진행 상황: {self.current_index + 1} / {len(self.questions)}")
            self.question_label.config(text=f"Q{self.current_index + 1}. {q_data['q']}")
            self.btn_a.config(text=q_data["A"])
            self.btn_b.config(text=q_data["B"])
        else:
            self.show_result()

    def process_answer(self, choice):
        # 점수 계산
        q_data = self.questions[self.current_index]
        selected_type = q_data[f"{choice}_type"]
        self.scores[selected_type] += 1
        
        # 다음 질문으로 이동
        self.current_index += 1
        self.update_question()

    def show_result(self):
        # 결과 계산 로직
        result_type = ""
        result_type += "E" if self.scores["E"] > self.scores["I"] else "I"
        result_type += "S" if self.scores["S"] > self.scores["N"] else "N"
        result_type += "T" if self.scores["T"] > self.scores["F"] else "F"
        result_type += "J" if self.scores["J"] > self.scores["P"] else "P"

        # 화면 클리어 (기존 위젯 숨기기)
        self.progress_label.pack_forget()
        self.question_label.pack_forget()
        self.btn_a.master.pack_forget() # 버튼 프레임 전체 숨기기

        # 결과 화면 표시
        result_title = tk.Label(self.root, text=f"당신의 유형은\n[{result_type}] 입니다!", font=("Arial", 24, "bold"), fg="#2E7D32")
        result_title.pack(pady=40)

        desc_text = self.results_desc.get(result_type, "결과 없음")
        result_desc = tk.Label(self.root, text=desc_text, font=("Arial", 14), wraplength=500, justify="center", bg="#f1f8e9", padx=20, pady=20)
        result_desc.pack(pady=20)

        # 종료 버튼
        quit_btn = tk.Button(self.root, text="종료하기", command=self.root.quit, width=20, height=2, bg="#ffcdd2")
        quit_btn.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = MBTIGUI(root)
    root.mainloop()