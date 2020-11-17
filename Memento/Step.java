

import java.util.Date;


public class Step {
    private String num;
    private Date date;

    public void setStep(String num) {
        this.num = num;
        this.date = new Date();
    }

    public Save save() {
        return new Save(num);
    }

    public void load(Save save) {
        date = save.getDate();
        num  = save.getNum();
    }
    
    @Override
    public String toString() {
        return "Step: " + num + "\nDate: " + date + "\n";
    }
}