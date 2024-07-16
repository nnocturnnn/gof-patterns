
public class  WikiFactory {
    WikiPrototype prototype;

    public WikiFactory(WikiPrototype prototype) {
        this.prototype = prototype;
    }
    public void setPrototype(WikiPrototype prototype) {
        this.prototype = prototype;
    }
    WikiPrototype clonePrototype() {
        return (WikiPrototype) prototype.copy();
    }
 }