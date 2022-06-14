import genshinstats as gs
import time
import win10toast



#авторизация
gs.set_cookie_auto() # получаем куки с браузера
uid = 710785423  # ид игры
data = gs.get_user_stats(uid)
total_characters = len(data['characters'])
print("Авторизация.....")
toast = win10toast.ToastNotifier() # подключаем оповещение
toast.show_toast(title="GIMD", msg='Работает только с браузерами Chrome, Firefox, Opera, Edge, Chromium, and Brave. Если вы получили ошибку то вам стоит обратиться к https://t.me/PablooTish',icon_path="ge.ico")




#забираем дейлики
if __name__ == "__main__":
    while True:
        reward = gs.claim_daily_reward()
        if reward is not None:
            characters = gs.get_characters(uid)
            print(f"Забрал {reward['cnt']}x {reward['name']}")
            toast.show_toast(title='GIMD', msg= f"Забрал сегодня {reward['cnt']}x {reward['name']}", icon_path="ge.ico")
        else:
            print("Все забрал")
            toast.show_toast(title='GIMD', msg="Ты все забрал",icon_path="ge.ico")
        time.sleep(24 * 60 * 60 - 2)