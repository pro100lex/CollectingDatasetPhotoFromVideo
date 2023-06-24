from cv2 import cv2
import os


def take_screenshots_from_video(path_video, frequency_screenshot, playback_speed):
    """Функция составления датасета из указанного видео"""
    normalized_path = path_video.replace('"', '').replace('\\', '/')
    video_cap = cv2.VideoCapture(normalized_path)

    if not os.path.exists('dataset_from_video'):
        os.mkdir('dataset_from_video')

    counter_screenshots = 1

    while True:
        is_correct, frame = video_cap.read()
        fps = video_cap.get(cv2.CAP_PROP_FPS)
        multiplier = fps * frequency_screenshot

        if is_correct:
            frame_id = int(round(video_cap.get(1)))
            cv2.imshow('frame', frame)
            key = cv2.waitKey(playback_speed)

            if frame_id % multiplier == 0:
                cv2.imwrite(f"dataset_from_video/{normalized_path[normalized_path.rfind('/') + 1:normalized_path.rfind('.')]}_{counter_screenshots}.jpg", frame)
                print(f'Получен {counter_screenshots} скриншот')
                counter_screenshots += 1

            if key == ord(" "):
                cv2.imwrite(f"dataset_from_video/{normalized_path[normalized_path.rfind('/') + 1:normalized_path.rfind('.')]}_{counter_screenshots}_on_demand.jpg", frame)
                print(f'Получен {counter_screenshots} скриншот (по требованию)')
                counter_screenshots += 1

            elif key == ord('q'):
                print('Нажата клавиша Q, завершение процесса...')
                break

        else:
            print('[Ошибка] Невозможно получить кадр!')
            break

    video_cap.release()
    cv2.destroyAllWindows()


def main():
    path_video = input('Путь до видео из которого нужно получить датасет скриншотов: ')
    frequency_screenshot = int(input('Через сколько секунд будут делаться скриншоты: '))
    playback_speed = int(input('Скорость воспроизведения видео (чем ниже, тем быстрее): '))

    print('Для завершения процесса нажмите клавишу Q (Включить английскую раскладку)')

    take_screenshots_from_video(path_video=path_video, frequency_screenshot=frequency_screenshot, playback_speed=playback_speed)


if __name__ == '__main__':
    main()