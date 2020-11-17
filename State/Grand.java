

public class Grand {
    StateG stateG;

    public void setStateG(StateG stateG) {
        this.stateG = stateG;
    }

    public void changeState() {
        if (stateG instanceof Waity) {
            setStateG(new Accepted);
        } else if (stateG instanceof Aceepted) {
            setStateG(new Canceled);
        } else if (stateG instanceof Canceled) {
            setStateG(new Waity);
        }
    }

    public void whatStay() {
        stateG.whatStay();
    }
}