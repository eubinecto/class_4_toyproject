

from transformers import pipeline, Conversation


def main():
    # 우리의 목표 = 간단한
    # 하나의 시나리오.
    conversational_pipeline = pipeline("conversational")
    conv = Conversation("Can you guess what fruit I'm thinking of?")
    conv.add_user_input("What color is your fruit?")  # 봇이 이런말을 할 것이다.
    conv.append_response(response="I'm thinking of a red fruit")
    res = conversational_pipeline([conv])
    print(res)


if __name__ == '__main__':
    main()