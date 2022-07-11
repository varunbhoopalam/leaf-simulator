from enum import Enum


class LeafState(Enum, str):
    bud = "bud"  # leaf taking energy from tree
    open = "open"  # leaf giving energy to tree from sun
    detached = "detached"  # no longer on the tree


class Leaf:
    state: str

    def __init__(self):
        self.state = LeafState.bud

    def photosynthesize(self, sun_exposure, moisture_content):
        """
        The process with which leaves
        :param sun_exposure:
        :param moisture_content:
        :return:
        """
        pass

    def transpiration(self):
        """
        The process by which leaves help trees release moisture
        :return:
        """


class EvergreenLeaf(Leaf):
    """
    These leaves grow and fall without relation to the seasons
    """
    pass


class DeciduousLeaf(Leaf):
    """
    These leaves grow and fall seasonally
    """

    def get_color(self):
        """
        The color of a deciduous leaf is driven by the chlorophyll in the leaf?
        Apparently a chemical called anthocyanin may also be involved.
        :return:
        """
        pass
