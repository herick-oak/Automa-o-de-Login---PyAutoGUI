import pyautogui as pg
import time

pg.PAUSE = 0.5

# abrir o opera
time.sleep(2)
pg.press("win")
pg.write("Opera")
pg.press("enter")

#entrar no site
time.sleep(2)
pg.write("https://on.fiap.com.br")
pg.press("enter")


#fazer o login
time.sleep(2)
pg.click(x=972, y=548)
pg.write("Adicioneseuemail@gmail.com")
pg.click(x=965, y=635)
pg.write("Adicionesuasenha1234")
pg.click(x=960, y=684)
pg.press("enter")
