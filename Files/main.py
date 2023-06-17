import pyautogui


def start_search(search):
    search_box_x_coord = 380
    search_box_y_coord = 185
    control_key = "ctrl"
    a_key = "a"
    backspace_key = "backspace"
    enter_key = "enter"
    pyautogui.sleep(2)
    for item in search:
        pyautogui.sleep(2)
        pyautogui.click(search_box_x_coord, search_box_y_coord)
        pyautogui.hotkey(control_key, a_key)
        pyautogui.press(backspace_key)
        pyautogui.write(item)
        pyautogui.press(enter_key)


if __name__ == "__main__":
    search = ["how to turn off bing search history", "what is chatgpt", "leetcode", "codeforces", "Python documentation"
              "what are the lastest news", "sports", "what is cubing", "how to get free microsoft points", "Hello world", 
              "bit manipilation", "binary trees", "segmentation trees", "graphs", "bfs", "dfs", "maths for cp", "cses fi", 
              "sub sequence", "red coder on cf", "greedy algorithms", "binary search", "dynamic programming", "AIML", "SVM", 
              "K means ", "KNN", "ANN", "CNN","hashmap in c++" ,"how to code like tourist"]
    start_search(search)
