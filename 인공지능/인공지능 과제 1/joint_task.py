import util
import wordsegUtil


class JointSegmentationInsertionProblem(util.SearchProblem):
    def __init__(self, query, bigramCost, possibleFills):
        self.query = query
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def start_state(self):
        return 0, wordsegUtil.SENTENCE_BEGIN  # position before which text is reconstructed & previous word

    def is_end(self, state):
        return state[0] == len(self.query)

    def succ_and_cost(self, state):
        # BEGIN_YOUR_CODE
        pos, prev_word = state
        for step in range(1, len(self.query)- pos + 1):
            vowel_removed_word = self.query[pos:pos+step]
            fills = self.possibleFills(vowel_removed_word)
            for fill in fills:
                next_state = pos+step, fill
                cost = self.bigramCost(prev_word, fill)
                yield fill, next_state, cost
    

        # HINT:
        #   for each possible segmentation:
        #     for each possible insertion:
        #       yield action, succ, cost
        #raise NotImplementedError('not implemented')
        # END_YOUR_CODE


if __name__ == '__main__':
    unigramCost, bigramCost = wordsegUtil.makeLanguageModels('leo-will.txt')
    smoothCost = wordsegUtil.smoothUnigramAndBigram(unigramCost, bigramCost, 0.2)
    possibleFills = wordsegUtil.makeInverseRemovalDictionary('leo-will.txt', 'aeiou')
    # problem = JointSegmentationInsertionProblem('aeronauticalengineering', smoothCost, possibleFills)
    problem = JointSegmentationInsertionProblem(wordsegUtil.removeAll('whatsup', 'aeiou'), smoothCost, possibleFills)

    # import dynamic_programming_search
    # dps = dynamic_programming_search.DynamicProgrammingSearch(verbose=1)
    # # dps = dynamic_programming_search.DynamicProgrammingSearch(memory_use=False, verbose=1)
    # print(dps.solve(problem))

    import uniform_cost_search
    ucs = uniform_cost_search.UniformCostSearch(verbose=0)
    print(ucs.solve(problem))


# === Other Examples ===
# 
# QUERIES_BOTH = [
# 'stff' => ['staff']
# 'hllthr' => ['hill', 'there']
# 'thffcrndprncndrw' => ['the', 'officer', 'and', 'prince', 'andrew']
# 'thstffffcrndprncndrwmntdthrhrssndrdn' => ['the', 'staff', 'officer', 'and', 'prince', 'andrew', 'mounted', 'their', 'horses', 'under', 'done']
# 'whatsup' => ['whats', 'up']
# 'ipovercarrierpigeon' => ['pauvre', 'carrier', 'up', 'again']
# 'aeronauticalengineering' => ['arent', 'clean', 'ignoring']
# 'themanwiththegoldeneyeball' => ['the', 'man', 'with', 'the', 'golden', 'eyeball']
# 'lightbulbsneedchange' => ['light', 'blue', 'bees', 'and', 'change']
# 'internationalplease' => ['international', 'please']
# 'comevisitnaples' => ['come', 'visit', 'naples']
# 'somethingintheway' => ['something', 'in', 'the', 'way']
# 'itselementarymydearwatson' => ['its', 'elementary', 'my', 'drew', 'its', 'in']
# 'itselementarymyqueen' => ['its', 'elementary', 'my', 'queen']
# 'themanandthewoman' => ['the', 'man', 'and', 'the', 'woman']
# 'nghlrdy' => ['enough', 'already']
# 'jointmodelingworks' => ['joint', 'modeling', 'works']
# 'jointmodelingworkssometimes' => ['joint', 'modeling', 'works', 'sometimes']
# 'jointmodelingsometimesworks' => ['joint', 'modeling', 'sometimes', 'works']
# 'rtfclntllgnc' => ['artificial', 'intelligence']
# ]
