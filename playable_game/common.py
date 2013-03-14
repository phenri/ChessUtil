import functools
from collections import namedtuple


WHITE = 1
NONE = 0
BLACK = -1


_bool_or_none_to_color_map = {
	True: WHITE,
	False: BLACK,
	None: NONE
}


PromotionMoveInfo = namedtuple('MoveInfo', ['source', 'destination', 'promotion'])
MoveInfo = functools.partial(PromotionMoveInfo, promotion=None)


def make_eight(item):
	return [item for _ in range(8)]


def opponent_of(color):
	return color * -1


class ActiveColorError(Exception): pass
class IllegalMoveError(Exception): pass
class IllegalSquareError(Exception): pass
class InvalidNotationError(Exception): pass
class PieceNotFoundError(Exception): pass