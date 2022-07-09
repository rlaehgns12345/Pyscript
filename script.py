import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = https://www.facebook.com/profile.php?id=100044991190714
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["blue", "white"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "김도훈")
write("description", "07년생")
write("button", "페북")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "사는 곳": "수성구",:	
  "중학교": "동부중",
  "생년월일": "07/10/12",
  "좋아하는 것": "게임",
}
information(informations)