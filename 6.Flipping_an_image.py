class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        flipped_and_inverted_image = []
        for single_list in A:
            flipped_image = single_list[::-1]
            for i in range(len(flipped_image)):
                if flipped_image[i] == 1:
                    flipped_image[i] = 0
                else:
                    flipped_image[i] = 1
            flipped_and_inverted_image.append(flipped_image)
        return flipped_and_inverted_image
