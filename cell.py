from graphics import *

class Cell():
    def __init__(self,point1,point2,left=True,right=True,top=True,bottom=True):
        self.__x1 = point1.x
        self.__x2 = point2.x
        self.__y1 = point1.y
        self.__y2 = point2.y
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom

    def draw(self,canvas,fill_color):
        if self.has_left_wall:
            left_wall = Line(Point(self.__x1,self.__y1),Point(self.__x1,self.__y2))
            canvas.create_line(self.__x1,self.__y1,self.__x1,self.__y2,fill=fill_color,width=4)
        if self.has_right_wall:
            right_wall = Line(Point(self.__x2,self.__y1),Point(self.__x2,self.__y2))
            canvas.create_line(self.__x2,self.__y1,self.__x2,self.__y2,fill=fill_color,width=4)
        if self.has_top_wall:
            top_wall = Line(Point(self.__x1,self.__y1),Point(self.__x2,self.__y1))
            canvas.create_line(self.__x1,self.__y1,self.__x2,self.__y1,fill=fill_color,width=4)
        if self.has_bottom_wall:
            left_wall = Line(Point(self.__x1,self.__y2),Point(self.__x2,self.__y2))
            canvas.create_line(self.__x1,self.__y2,self.__x2,self.__y2,fill=fill_color,width=4)
