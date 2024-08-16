import os

from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# .env dosyasını yüklüyoruz
load_dotenv()

# OpenAI API anahtarını alıyoruz
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(api_key=openai_api_key, model="gpt-3.5-turbo")

memory = ConversationBufferMemory()

# Prompt şablonunu tanımlıyoruz
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="""
        Sen sadece Ankara hakkında bilgi sağlayan bir gezi rehberisin. 
        Eğer soru Ankara ile ilgili değilse, 'Bu soruya cevap veremem. Lütfen sadece Başkent ile ilgili soru sorunuz' diye yanıt ver. 
        Her zaman Türkçe cevap ver. 
        İşte kullanıcının sorusu: {question}
    """,
)

# Zinciri (chain) oluşturuyoruz
chain = LLMChain(llm=llm, prompt=prompt_template, memory=memory)


def main():
    while True:
        # Kullanıcıdan bir soru alıyoruz
        question = input("Sorunuzu girin (çıkmak için 'exit' yazın): ")

        if question.lower() == "exit":
            print("AnkarAI'yi kullandığınız için teşekkürler!")
            break

        # Soruyu zincire gönderiyoruz ve yanıtı alıyoruz
        response = chain.invoke({"question": question})

        # Response içerisindeki doğru key'e ulaşmak için response'u kontrol edelim
        if isinstance(response, dict):
            # Eğer response bir dict ise ve 'text' anahtarı varsa onu alalım
            answer = response.get("text", "Bir hata oluştu, lütfen tekrar deneyin.")
        else:
            # Eğer response beklenen formatta değilse, varsayılan bir mesaj
            answer = "Bir hata oluştu, lütfen tekrar deneyin."

        print(f"Cevap: {answer}\n")


if __name__ == "__main__":
    main()
