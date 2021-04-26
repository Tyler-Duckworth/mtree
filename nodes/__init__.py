from .node_tree import classes as node_tree_classes
from .trunk_node import MtreeTrunk, MTREE_OT_UpdateGreasePencil
from .grow_node import MtreeGrow
from .split_node import MtreeSplit
from .branch_node import MtreeBranch
from .root_node import MtreeRoots
from .tree_parameters_node import MtreeParameters, MTREE_OT_ExecuteNodeTree, MTREE_OT_Randomize, MTREE_OT_ResetActiveTree
from .twig_node import MTREE_OT_SpawnTwig, MtreeTwig

nodes_classes = node_tree_classes + [MtreeTrunk, MtreeGrow, MtreeParameters, MTREE_OT_ExecuteNodeTree,
                                     MtreeSplit, MtreeBranch, MTREE_OT_SpawnTwig, MtreeTwig, MTREE_OT_Randomize,
                                     MtreeRoots, MTREE_OT_ResetActiveTree, MTREE_OT_UpdateGreasePencil]