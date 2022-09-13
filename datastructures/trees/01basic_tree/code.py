from typing import List

class TreeNode():

    def __init__(self, data, children:List["TreeNode"]=None):
        self.data = data
        self.children:List["TreeNode"] = children


    def addChild(self, treeNode:List["TreeNode"]):
        self.children.append(treeNode)


    def __str__(self, level=0):
        startwith = " " if level == 0 else "--"
        ret = (startwith * level)+'> ' +str(self.data) +"\n"

        try:
            iterator = iter(self.children)
        except TypeError:
            # not iterable
            ret +=''
        else:
           # iterable
           for child in self.children:
            ret += child.__str__(level + 1)

        return ret




#Testing
tree = TreeNode('Drinks',[])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
tree.addChild(cold)
tree.addChild(hot)

tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
hot.addChild(tea)
hot.addChild(coffee)

alcholic = TreeNode('Alcholic', [])
non_alcholic = TreeNode('Non Alcoholic', [])
cold.addChild(alcholic)
cold.addChild(non_alcholic)

green = TreeNode('Green')
black = TreeNode('Black')
masala = TreeNode('Masala')
tea.addChild(green)
tea.addChild(black)
tea.addChild(masala)


latte = TreeNode('Latte')
cappuccino = TreeNode('Bru')
expresso = TreeNode('Coffee')
coffee.addChild(latte)
coffee.addChild(cappuccino)
coffee.addChild(expresso)

vine = TreeNode('Vine')
beer = TreeNode('Beer')
alcholic.addChild(vine)
alcholic.addChild(beer)

coke = TreeNode('Coke')
fanta = TreeNode('Fanta')
soda = TreeNode('Soda')
non_alcholic.addChild(coke)
non_alcholic.addChild(fanta)
non_alcholic.addChild(soda)
print(tree)
