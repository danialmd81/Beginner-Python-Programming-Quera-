words = input().split()

if words[0] == "havij" and words[1] == "havij":
    print("eyes!")
elif (words[0] == "shalgham" and words[1] == "shalgham") or (
    words[0] == "shalgham" and words[2] == "shalgham"
):
    print("cold!")
else:
    print("dead")
