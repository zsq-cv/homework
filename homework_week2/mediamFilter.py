import cv2
import numpy as np

def mid_filter(data,width,height,n):
    tmp=np.zeros(shape=(width-n+1,height-n+1))
    for i in range(0,height-n+1):
        for j in range(0,width-n+1):
            modle = data[i:i+n]
            modle = modle[:,j:j+n]
            modle = modle.flatten()
            mid = mid_sort(modle)
            # tmp[i+int((n-1)/2)-1,j+int((n-1)/2)-1] = mid
            tmp[i,j]=mid
    return tmp
# def flatten(matrix):
#     w=len(matrix)
#     h=len(matrix[0])
#     tmp=[]
#     for i in range(w):
#         for j in range(h):
#             tmp.append(matrix[i][j])
#     return tmp
def mid_sort(data):
    data.sort()
    return data[len(data)//2]

# data=np.array([[1,2,3,1],[3,5,2,6],[2,4,1,7],[3,5,4,2]])


img=cv2.imread('D:\kaikeba_5th\CV\week 2\lenna.jpg')
# print(img)
b,g,r = cv2.split(img)
# print(cv2.split(img))
# cv2.imshow('BLUE',b)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
w,h = gray.shape
# print(gray.shape)
med_gray = mid_filter(gray,w,h,3)
# cv2.imshow("med_gray",med_gray)
# gray=gray[0:300,100:200]
width_b,height_b=b.shape
width_g,height_g=g.shape
width_r,height_r=r.shape
output_b=mid_filter(b,width_b,height_b,3)
output_g=mid_filter(g,width_g,height_g,3)
output_r=mid_filter(r,width_r,height_r,3)
merge=cv2.merge([output_b,output_g,output_r])
merge_out = merge.astype(np.float32) / 255
md_img = cv2.medianBlur(img, 7)
print(merge.dtype)
print(type(output_r))
print(output_r)
cv2.imshow('output_r',output_r/256)
# print(cv2.split(md_img))
cv2.imshow('md_lenna',md_img)
# cv2.imshow('gray',gray)
cv2.imshow('mediamFilter',merge_out)
key=cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()

