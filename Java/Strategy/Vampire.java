

public class Vampire {
    Activity activity;

    public void setActivity(Activity activity) {
        this.activity =  activity;
    }

    public void executeActivity() {
        activity.justDoIt();
    }
}