int reverse(int x){
    int reversed = 0;
    int mod = 0;

    if (x > pow(2, 31) - 1 && x < -(pow(2, 31))) {
	    return 0;
    }

    while (x != 0) {
	    mod = x % 10;
	    if (reversed > (pow(2, 31) - 1) / 10 || reversed < -(pow(2, 31) / 10)) {
		    return 0;
	    }
	    reversed = reversed * 10 + mod;
	    x /= 10;
    }
    return reversed;
}
