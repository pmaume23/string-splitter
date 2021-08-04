class TagManipulator():    
    def parse_string(self, tags):
        result = []

        if len(tags) < 1 :
            return result

        return result


    def test_split_comma_empty_string_result_empty_array():
    # arrange
        stringToSplit = ","
        expResult = []
        result = None
        cut = TagManipulator()

    # act
        result = cut.parse_string(stringToSplit)

    # assert
        assert result == expResult