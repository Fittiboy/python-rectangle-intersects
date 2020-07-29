class Rectangle:
    def __init__(self, left=0, top=0, right=0, bottom=0):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        left = str(self.left)
        top = str(self.top)
        right = str(self.right)
        bottom = str(self.bottom)
        return f"({left}, {top}), ({right}, {bottom})"

    def is_positive(self):
        return self.left < self.right and self.bottom < self.top

    def intersect(self, r):
        left = max(self.left, r.left)
        top = min(self.top, r.top)
        right = min(self.right, r.right)
        bottom = max(self.bottom, r.bottom)

        intersect_ = Rectangle(left, top, right, bottom)

        if intersect_.is_positive():
            return intersect_
        else:
            return Rectangle()


def multi_rects_intersect(*rects):
    if len(rects) == 0:
        return Rectangle()
    elif len(rects) == 1:
        return rects[0]
    else:
        first_ints = rects[0].intersect(rects[1])
        return multi_rects_intersect(first_ints, *rects[2:])


if __name__ == "__main__":
    rect1 = Rectangle(-2, 2, 2, -2)
    rect2 = Rectangle(0, 0, 2, -2)
    rect3 = Rectangle(0, 0, 1, -1)
    rect4 = Rectangle(10, 10, 11, 9)
    rect5 = Rectangle(8, 11, 12, 8)
    rect6 = Rectangle(0, 100, 10, 0)

    print(multi_rects_intersect(rect1, rect2, rect3))
    print(multi_rects_intersect(rect1, rect2, rect3, rect4))
    print(multi_rects_intersect())
    print(multi_rects_intersect(rect1, rect2))
    print(multi_rects_intersect(rect4, rect5))
    print(multi_rects_intersect(rect4, rect6))
