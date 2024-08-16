
# AnkarAI - Ankara Gezi Rehberi

**AnkarAI**, Ankara hakkında bilgi sağlayan yapay zeka destekli bir gezi rehberidir. Bu proje, OpenAI'nin GPT-3.5-Turbo modelini kullanarak kullanıcıların Ankara ile ilgili sorularını yanıtlayan bir web uygulaması sunmaktadır. 

## Özellikler

- **Türkçe Yanıtlar:** Uygulama yalnızca Türkçe yanıtlar verir.
- **Ankara Odaklı:** Sadece Ankara ile ilgili sorulara yanıt verir. Ankara dışındaki sorulara "Bu soruya cevap veremem." şeklinde yanıt verir.
- **Teşekkür Mesajı:** Her cevabın sonunda otomatik olarak "AnkarAI kullandığınız için teşekkür ederim." mesajı eklenir.

## Kurulum

### Gereksinimler

- Python 3.10+
- Flask
- OpenAI API Anahtarı

### Adım 1: Depoyu Klonlayın

Öncelikle, bu projeyi kendi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/barancanercan/AnkarAI.git
cd AnkarAI
```

### Adım 2: Sanal Ortam Oluşturun ve Etkinleştirin

```bash
python -m venv env
source env/bin/activate  # Linux/MacOS
# veya
env\Scriptsctivate  # Windows
```

### Adım 3: Gerekli Kütüphaneleri Yükleyin

```bash
pip install -r requirements.txt
```

### Adım 4: OpenAI API Anahtarını Ayarlayın

API anahtarınızı bir `.env` dosyasına ya da terminal ortam değişkeni olarak ekleyin:

```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

### Adım 5: Uygulamayı Başlatın

```bash
python app.py
```

Uygulama, `http://127.0.0.1:5000/` adresinde çalışacaktır.

## Kullanım

- **Ana Sayfa:** Ana sayfada, kullanıcılar Ankara hakkında sorularını girer ve "Soru Sor" butonuna basarlar.
- **Yanıt:** Uygulama, soruya uygun olarak Türkçe yanıt verir ve yanıtın sonunda "AnkarAI kullandığınız için teşekkür ederim." mesajı eklenir.

## Dosya Yapısı

```plaintext
AnkarAI/
│
├── templates/
│   └── index.html         # HTML dosyası
├── static/
│   └── styles.css         # CSS dosyası
├── app.py                 # Flask uygulaması
├── ankarai.py             # AnkarAI backend kodu
├── README.md              # Bu dökümantasyon dosyası
└── requirements.txt       # Gerekli Python kütüphaneleri
```

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir pull request gönderin. Her türlü katkı memnuniyetle karşılanır!

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.
