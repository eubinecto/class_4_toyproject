
from transformers.pipelines import pipeline
from transformers import Conversation


def main():
    # conversational pipeline 설치.
    conversational_pipeline = pipeline("conversational")
    # 내가 생각하고 있는 과일을 맞춰볼래?
    conv_1 = Conversation("Can you guess what fruit I'm thinking of?")
    conv_2 = Conversation("What color is your fruit?")
    conv_3 = Conversation("I'm thinking of a red fruit. Can you guess what it is?")
    # 이런식으로 대화를 진행하는 것 같다?
    res = conversational_pipeline([conv_1, conv_2, conv_3])
    print(res)


if __name__ == '__main__':
    main()

