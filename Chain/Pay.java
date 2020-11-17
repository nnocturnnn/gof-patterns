
public abstract class Pay {
    private int priority;
    private Terminal nextTerminal;

    public Pay(int priority) {
        this.priority = priority;
    }

    public void setNextPay(Terminal terminal) {
        this.nextTerminal = terminal;
    }

    public void PayManager
}