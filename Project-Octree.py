class Node:
    def __init__(self, root, Xupl, Yupl, Zupl, Xlowl, Ylowl, Zlowl):
        self.root = root
        self.Xupl = Xupl
        self.Yupl = Yupl
        self.Zupl = Zupl
        self.Xlowl = Xlowl
        self.Ylowl = Ylowl
        self.Zlowl = Zlowl
        self.Xcenter = (self.Xupl + self.Xlowl) / 2.
        self.Ycenter = (self.Yupl + self.Ylowl) / 2.
        self.Zcenter = (self.Zupl + self.Xlowl) / 2.

    root = None


    # children
    QuadI = None
    QuadII = None
    QuadIII = None
    QuadIV = None
    QuadV = None
    QuadVI = None
    QuadVII = None
    QuadVIII = None

    Xupl = None
    Yupl = None
    Zupl = None

    Xlowl = None
    Ylowl = None
    Zlowl = None


    def add(self, coord, level):

        if level == 0:
           self.value = []
           self.value.append((coord))

        else:
            level -= 1
            # Determine quadrant
            if coord[0] <= self.Xcenter:
                # negX
                if coord[1] <= self.Ycenter:
                    # negY
                    if coord[2] <= self.Zcenter:
                        # negZ
                        Xupl = self.Xcenter
                        Yupl = self.Ycenter
                        Zupl = self.Zcenter
                        Xlowl = self.Xlowl
                        Ylowl = self.Ylowl
                        Zlowl = self.Zlowl
                        self.QuadVIII = Node(self.QuadVIII, Xupl, Yupl, Zupl, Xlowl,
                                                 Ylowl, Zlowl)
                        self.QuadVIII.add(coord, level)
                    else:
                        # posZ
                        Xupl = self.Xcenter
                        Yupl = self.Ycenter
                        Zupl = self.Zupl
                        Xlowl = self.Xlowl
                        Ylowl = self.Ylowl
                        Zlowl = self.Zcenter
                        self.QuadVII = Node(self.QuadVIII, Xupl, Yupl, Zupl, Xlowl,
                                                 Ylowl, Zlowl)
                        self.QuadVII.add(coord, level)
                else:
                    # posY
                    if coord[2] <= self.Zcenter:
                        # negZ
                        Xupl = self.Xcenter
                        Yupl = self.Yupl
                        Zupl = self.Zcenter
                        Xlowl = self.Xlowl
                        Ylowl = self.Ycenter
                        Zlowl = self.Zlowl
                        self.QuadVI = Node(self.QuadVIII, Xupl, Yupl, Zupl, Xlowl,
                                                 Ylowl, Zlowl)
                        self.QuadVI.add(coord, level)

                    else:
                        # posZ
                        Xupl = self.Xcenter
                        Yupl = self.Yupl
                        Zupl = self.Zupl
                        Xlowl = self.Xlowl
                        Ylowl = self.Ycenter
                        Zlowl = self.Zcenter
                        self.QuadV = Node(self.QuadVIII, Xupl, Yupl, Zupl, Xlowl,
                                                 Ylowl, Zlowl)
                        self.QuadV.add(coord, level)


            else:
                # posX
                if coord[1] <= self.Ycenter:
                    # negY
                    if coord[2] <= self.Zcenter:
                        # negZ
                        Xupl = self.Xupl
                        Yupl = self.Ycenter
                        Zupl = self.Zcenter
                        Xlowl = self.Xcenter
                        Ylowl = self.Ylowl
                        Zlowl = self.Zlowl
                        self.QuadIV = Node(self.QuadVIII, Xupl, Yupl, Zupl, Xlowl, Ylowl, Zlowl)
                        self.QuadIV.add(coord, level)

                    else:
                        # posZ
                        Xupl = self.Xupl
                        Yupl = self.Ycenter
                        Zupl = self.Zupl
                        Xlowl = self.Xcenter
                        Ylowl = self.Ylowl
                        Zlowl = self.Zcenter
                        self.QuadIII = Node(self.QuadVIII, Xupl, Yupl, Zupl, Xlowl,Ylowl, Zlowl)
                        self.QuadIII.add(coord, level)

                else:
                    # posY
                    if coord[2] <= self.Zcenter:
                        # negZ
                        Xupl = self.Xupl
                        Yupl = self.Yupl
                        Zupl = self.Zcenter
                        Xlowl = self.Zcenter
                        Ylowl = self.Ycenter
                        Zlowl = self.Zlowl
                        self.QuadII = Node(self.QuadVIII, Xupl, Yupl, Zupl, Xlowl,
                                                 Ylowl, Zlowl)
                        self.QuadII.add(coord, level)

                    else:
                        # posZ
                        Xupl = self.Xupl
                        Yupl = self.Yupl
                        Zupl = self.Zupl
                        Xlowl = self.Xcenter
                        Ylowl = self.Ycenter
                        Zlowl = self.Zcenter
                        self.QuadI = Node(self.QuadVIII, Xupl, Yupl, Zupl, Xlowl,
                                                 Ylowl, Zlowl)
                        self.QuadI.add(coord, level)


class Octree():
    """
    class to hold the whole tree
    """

    def __init__(self, Xmax, Ymax, Zmax, rootcord=(0, 0, 0), maxnode=7):
        self.Xmax = Xmax
        self.Ymax = Ymax
        self.Zmax = Xmax
        self.Xmin = -Xmax
        self.Ymin = -Ymax
        self.Zmin = -Zmax
        self.rootcord = rootcord
        self.maxnode = maxnode

        self.root = Node('root', Xmax, Ymax, Zmax, -Xmax, -Ymax, -Zmax)

    def addnode(self, coord):
        if(coord[0]>worldsize or coord[1]>worldsize or coord[2]>worldsize):
            print("Out of bounds")
        else:
            self.root.add(coord, self.maxnode)

    def search(self, center, size):
            coordinates = []
            templist = [self.root]
            list = []
            list.append([self.root])
            for level in range(self.maxnode):
                list.append([])

            for level in range(self.maxnode):
                for Node in list[level]:
                    corner0 = (center[0] + size, center[1] + size, center[2] + size)
                    corner1 = (center[0] + size, center[1] + size, center[2] + size)
                    corner2 = (center[0] + size, center[1] - size, center[2] + size)
                    corner3 = (center[0] + size, center[1] - size, center[2] - size)
                    corner4 = (center[0] - size, center[1] + size, center[2] + size)
                    corner5 = (center[0] - size, center[1] + size, center[2] - size)
                    corner6 = (center[0] - size, center[1] - size, center[2] + size)
                    corner7 = (center[0] - size, center[1] - size, center[2] - size)
                    corners = [corner0, corner1, corner2, corner3, corner4, corner5, corner6, corner7]
                    table = ((corner0[0] > Node.Xcenter), (corner0[1] > Node.Ycenter), (corner0[2] > Node.Zcenter))
                    if False not in table:
                        list[level + 1].append(Node.QuadI)
                    table = ((corner1[0] > Node.Xcenter), (corner1[1] > Node.Ycenter), (corner1[2] < Node.Zcenter))
                    if not False in table:
                        list[level + 1].append(Node.QuadII)
                    table = ((corner2[0] > Node.Xcenter), (corner2[1] < Node.Ycenter), (corner2[2] > Node.Zcenter))
                    if not False in table:
                        list[level + 1].append(Node.QuadIII)
                    table = ((corner3[0] > Node.Xcenter), (corner3[1] < Node.Ycenter), (corner3[2] < Node.Zcenter))
                    if not False in table:
                        list[level + 1].append(Node.QuadIV)
                    table = ((corner4[0] < Node.Xcenter), (corner4[1] > Node.Ycenter), (corner4[2] > Node.Zcenter))
                    if not False in table:
                        list[level + 1].append(Node.QuadV)
                    table = ((corner5[0] < Node.Xcenter), (corner5[1] > Node.Ycenter), (corner5[2] < Node.Zcenter))
                    if not False in table:
                        list[level + 1].append(Node.QuadVI)
                    table = ((corner6[0] < Node.Xcenter), (corner6[1] < Node.Ycenter), (corner6[2] > Node.Zcenter))
                    if not False in table:
                        list[level + 1].append(Node.QuadVII)
                    table = ((corner7[0] < Node.Xcenter), (corner7[1] < Node.Ycenter), (corner7[2] < Node.Zcenter))
                    if not False in table:
                        list[level + 1].append(Node.QuadVIII)
                    temp_templist = []
                    for Node in list[level + 1]:
                        try:
                            Node.Xcenter
                            temp_templist.append(Node)
                        except AttributeError:
                            pass
                    list[level + 1] = temp_templist

            cordinates = [i.value for i in list[-1]]
            return cordinates


worldsize = 100
tree = Octree(worldsize,worldsize,worldsize)
tree.addnode((-25,35,45))
tree.addnode((5,5,5))
tree.addnode((7,7,7))
tree.addnode((9,9,9))
entries = tree.search((0, 0, 0), 100)
for i in entries:
    print(i)