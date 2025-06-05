from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

# Uygulama penceresinin boyutunu ayarlıyoruz (genişlik, yükseklik)
Window.size = (325, 475)


class AnaPencere(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        # Sonuç ekranını oluşturuyoruz
        self.sonuc_ekrani = TextInput(
            font_size=40,
            size_hint_y=0.2,
            readonly=True,
            halign="right",
            multiline=False,
            background_color=[0.2, 0.2, 0.2, 1],
            foreground_color=[1, 1, 1, 1],
        )
        self.add_widget(self.sonuc_ekrani)

        # Butonları oluşturmak için bir liste tanımlıyoruz
        buton_listesi = [
            ['%', '+/-', '/', 'C'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['00', '0', '.', '=']
        ]

        # Butonları yerleştirmek için ızgara düzeni oluşturuyoruz
        buton_izgarasi = GridLayout(cols=4, spacing=5, padding=10)

        # Buton listesindeki her öğe için döngü oluşturuyoruz
        for satir in buton_listesi:
            for buton_etiketi in satir:
                buton = Button(
                    text=buton_etiketi,
                    font_size=32,
                    background_color=self.buton_rengi_ayarla(buton_etiketi),
                    on_press=self.butona_tiklandi
                )
                buton_izgarasi.add_widget(buton)

        self.add_widget(buton_izgarasi)

    # Buton renklerini ayarlayan fonksiyon
    def buton_rengi_ayarla(self, etiket):
        if etiket in {'%', '+/-', '/', 'C'}:
            return [0.3, 0.8, 0.8, 1]
        elif etiket in {"*", "-", "+", "="}:
            return [0.1, 0.2, 0.5, 1]
        return [0.6, 0.8, 1, 1]

    # Buton tıklama olayını işleyen fonksiyon
    def butona_tiklandi(self, buton):
        metin = buton.text

        if metin == "C":
            self.sonuc_ekrani.text = ""
        elif metin == "=":
            self.hesapla()
        elif metin == "+/-":
            self.negatif_yap()
        elif metin == "%":
            self.yuzde_cevir()
        else:
            self.sonuc_ekrani.text += metin

    # Hesaplama fonksiyonu
    def hesapla(self):
        try:
            self.sonuc_ekrani.text = str(eval(self.sonuc_ekrani.text))
        except Exception:
            self.sonuc_ekrani.text = "HATA!"

    # Pozitif/Negatif değiştirme fonksiyonu
    def negatif_yap(self):
        if self.sonuc_ekrani.text:
            if self.sonuc_ekrani.text[0] == '-':
                self.sonuc_ekrani.text = self.sonuc_ekrani.text[1:]
            else:
                self.sonuc_ekrani.text = '-' + self.sonuc_ekrani.text

    # Yüzde işlemi fonksiyonu
    def yuzde_cevir(self):
        try:
            self.sonuc_ekrani.text = str(float(self.sonuc_ekrani.text) / 100)
        except ValueError:
            self.sonuc_ekrani.text = "HATA!"


# Ana uygulama sınıfı
class HesapMakinesiUygulamasi(App):
    def build(self):
        return AnaPencere()


if __name__ == "__main__":
    HesapMakinesiUygulamasi().run()
