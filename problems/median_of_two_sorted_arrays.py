from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Garantir que nums1 seja o menor array para reduzir a complexidade
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        len1, len2 = len(nums1), len(nums2)
        left, right = 0, len1  # Limites da busca binária

        while left <= right:
            # Particionar nums1 e nums2
            partition1 = (left + right) // 2
            partition2 = (len1 + len2 + 1) // 2 - partition1

            # Definir os valores ao redor das partições
            maxLeft1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float("inf") if partition1 == len1 else nums1[partition1]

            maxLeft2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float("inf") if partition2 == len2 else nums2[partition2]

            # Verificar se as partições são válidas
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Calcular a mediana dependendo do tamanho total ser par ou ímpar
                if (len1 + len2) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                # Reduzir a partição em nums1
                right = partition1 - 1
            else:
                # Aumentar a partição em nums1
                left = partition1 + 1

        # Caso nunca encontre uma partição válida (teoricamente impossível com entradas válidas)
        return 0.0
