from manim import *


class BubbleSortWithCode(Scene):
    def construct(self):
        self.pointer_color_j = RED
        self.pointer_color_j1 = GREEN
        self.box_color = BLUE
        self.nums = [5, 2, 6, 4, 1, 3]

        # Right half: Code
        code = [
            "def bubbleSort(arr):",
            "    n = len(arr)",
            "    for i in range(n):",
            "        for j in range(0, n-i-1):",
            "            if arr[j] > arr[j+1]:",
            "                arr[j], arr[j+1] = arr[j+1], arr[j]"
        ]
        self.code_mobj = VGroup(*[Tex(line).scale(0.8) for line in code]).arrange(DOWN,
                                                                                  aligned_edge=LEFT).to_edge(RIGHT).shift(2*UP)
        self.play(Write(self.code_mobj))

        # Left half: Animation
        self.showTitle("Bubble Sort")
        self.showArray(self.nums)
        self.bubbleSort(self.nums, self.values_mobj, self.boxes_mobj)

    def showTitle(self, titleText):
        title = Tex(titleText).to_edge(UP).scale(1.5)
        self.play(Write(title))
        self.wait()

    def buildArray(self, nums):
        boxes = []
        for i in range(len(nums)):
            boxes.append(Square(side_length=1, color=self.box_color).move_to(4 * LEFT + i * RIGHT))
        self.boxes = boxes

        values = []
        for i in range(len(nums)):
            numText = str(nums[i])
            values.append(Tex(numText).move_to(4 * LEFT + i * RIGHT))

        self.boxes_mobj = boxes_mobj = VGroup(*boxes)
        self.values_mobj = values_mobj = VGroup(*values)
        self.array_mobj = VGroup(boxes_mobj, values_mobj)
        return boxes_mobj, values_mobj

    def showArray(self, nums):
        boxes_mobj, values_mobj = self.buildArray(nums)
        self.play(
            AnimationGroup(
                *[Create(mob) for mob in boxes_mobj],
                *[Write(mob) for mob in values_mobj],
                run_time=5,
                lag_ratio=0.2
            )
        )

    def bubbleSort(self, nums, values_mobj, boxes_mobj):
        arrayObjs = list(zip(nums, values_mobj, boxes_mobj))
        n = len(arrayObjs)

        # Pointers for j and j+1
        self.pointer_j = Triangle(start_angle=PI/2, color=self.pointer_color_j).next_to(self.boxes[0], UP)
        self.pointer_j1 = Triangle(start_angle=PI/2, color=self.pointer_color_j1).next_to(self.boxes[1], UP)
        self.play(Create(self.pointer_j), Create(self.pointer_j1))

        # Outer loop
        for i in range(n):
            self.play(self.code_mobj[2].animate.set_color(YELLOW))
            self.wait()
            self.play(self.code_mobj[2].animate.set_color(WHITE))

            # Inner loop
            for j in range(0, n-i-1):
                self.play(self.code_mobj[3].animate.set_color(YELLOW))
                self.wait()
                self.play(self.code_mobj[3].animate.set_color(WHITE))

                # Comparison
                currNum, nextNum = arrayObjs[j][0], arrayObjs[j+1][0]
                if currNum > nextNum:
                    self.play(self.code_mobj[4].animate.set_color(YELLOW))
                    self.wait()
                    self.play(self.code_mobj[4].animate.set_color(WHITE))

                    # Swap
                    self.play(self.code_mobj[5].animate.set_color(YELLOW))
                    arrayObjs[j], arrayObjs[j+1] = arrayObjs[j+1], arrayObjs[j]
                    self.play(Swap(arrayObjs[j][1], arrayObjs[j+1][1]))
                    self.play(self.code_mobj[5].animate.set_color(WHITE))
                else:
                    self.play(self.code_mobj[4].animate.set_color(RED))
                    self.wait()
                    self.play(self.code_mobj[4].animate.set_color(WHITE))

                # Move pointers
                if j < n-i-2:
                    self.play(self.pointer_j.animate.next_to(self.boxes[j+1], UP),
                              self.pointer_j1.animate.next_to(self.boxes[j+2], UP))

            # Reset pointers
            self.play(self.pointer_j.animate.next_to(self.boxes[0], UP),
                      self.pointer_j1.animate.next_to(self.boxes[1], UP))

    def displayComparison(self, currNum, nextNum, currBox, nextBox):
        highlight = VGroup(currBox, nextBox)
        brace = Brace(highlight, DOWN)
        brace_text = Tex(f"{currNum} > {nextNum}").next_to(brace, DOWN)
        self.play(AnimationGroup(GrowFromCenter(brace), Write(brace_text)))
        self.play(FadeOut(brace), FadeOut(brace_text))
        currBox.set_color(self.box_color)
        nextBox.set_color(self.box_color)

    def shiftPointer(self):
        self.pointer.generate_target()
        self.pointer.target.shift(RIGHT)
        self.play(MoveToTarget(self.pointer))

    def resetPointer(self):
        self.pointer.generate_target()
        self.pointer.target.next_to(self.boxes[0], UP)
        self.play(MoveToTarget(self.pointer))
