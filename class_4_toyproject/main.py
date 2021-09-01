
from transformers import pipeline, Conversation
# 사전훈련된 모델을 로딩할 때 시간이 좀 걸리는 것을 보인다
conversational_pipeline = pipeline("conversational")


def main():
    global conversational_pipeline
    conv = Conversation()

    while True:
        text = input("Enter text:")
        if text == 'quit':
            break
        conv.add_user_input(text)
        # 출력이 리스트? 출력이 Conv 객체!
        # 그러면 기존의  conv 객체를 업데이트해주면 간단한 챗봇을 만들 수 있다.
        conv = conversational_pipeline([conv])
        print(conv)


if __name__ == '__main__':
    main()
