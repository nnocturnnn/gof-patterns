

public class StateGrant {
    public static void main(String[] args) {
        StateG stateG = new Accepted();
        Grand grand = new Grand();

        grand.setStateG(stateG);

        for (int i = 0; i < 10; i ++) {
            grand.whatStay();
            grand.changeState();
        }
    }
}