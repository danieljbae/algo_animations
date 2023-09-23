from manim import *


class Demo(Scene):
    def construct(self):
        #######################################
        # export to arrayObj.py
        self.pointer_color = YELLOW
        self.box_color = BLUE_C
        self.nums = [5, 2, 6, 4, 1, 3]  # simpleConfig
        #######################################
        self.showTitle("Bubble Sort")
        # self.showArray(self.nums)

        #######################################
        self.build_text()

    def showTitle(self, titleText):
        title = Text(titleText).to_edge(UP).scale(1.5)
        self.play(
            Write(title)
        )
        self.wait()

    def buildArray(self, nums):
        '''
        Builds array mobjects (boxes and text values)
        Packs array mobjects into VGroups
        '''

        # Build array box mobjects
        boxes = []
        for i in range(len(nums)):
            boxes.append(
                Square(side_length=1, color=self.box_color).move_to(2 * LEFT + i * RIGHT)
            )
        self.boxes = boxes

        # Build array value mobjects
        values = []
        for i in range(len(nums)):
            numText = str(nums[i])
            values.append(Text(numText).move_to(2 * LEFT + i * RIGHT))

        # Aggregate mobjects
        boxes_mobj = VGroup(*boxes)
        values_mobj = VGroup(*values)
        self.array_mobj = VGroup(boxes_mobj, values_mobj)
        return boxes_mobj, values_mobj

    def showArray(self, nums):
        '''
        Display creation of array
        '''
        boxes_mobj, values_mobj = self.buildArray(nums)
        self.play(
            AnimationGroup(
                *[Create(mob) for mob in boxes_mobj],
                *[Create(mob) for mob in values_mobj],
                run_time=5,
                lag_ratio=0.2
            )
        )

    def build_text(self):
        """
        build pseudocode text
        """

        # paragraph = Paragraph('for i in range(n):',
        #                       '\tfor j in range(n):',
        #                       '\t\t if nums[i] > nums[i+1]:')
        # self.play(Write(paragraph[0][:5]))

        text_loop1_a = Text("for")
        text_loop1_b = Text("i").set_color(GREEN)
        text_loop1_c = Text("in range(n):")
        x = VGroup(text_loop1_a, text_loop1_b, text_loop1_c).arrange(direction=RIGHT)
        self.play(
            Write(x),
        )
        self.wait()
        self.play(
            x[1].animate.shift(UP),
        )
        self.play(
            x[1].animate.shift(RIGHT),
        )
