def rgb(r, g, b):
    # your code here :)
    def to_hex(num):
        num = min(255, max(0, num))
        return format(num, '02X').upper()
    
    return to_hex(r) + to_hex(g) + to_hex(b)
  
  
 @test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Tests")
    def _():
        test.assert_equals(rgb(0, 0, 0), "000000", "testing zero values")
        test.assert_equals(rgb(1, 2, 3), "010203", "testing near zero values")
        test.assert_equals(rgb(255, 255, 255), "FFFFFF", "testing max values")
        test.assert_equals(rgb(254, 253, 252), "FEFDFC", "testing near max values")
        test.assert_equals(rgb(-20, 275, 125), "00FF7D", "testing out of range values")
