import javax.swing.*; //import all classes from swing package
import java.awt.Font;
//This class defines width and height. setPreferredSize function
import java.awt.Dimension;

/*
 * package private(default access modifier) class
 * sets up UI for form
 */
class Form{
    private static JPanel panel;

    public static void main(String[] args){
        //create main/root frame
        JFrame frame = new JFrame();
        //creating a panel to store components
        panel = new JPanel();
        //null layout manager to make position absolute 
        //instead of relative
        panel.setLayout(null);
        setLabel("Register User",30,218,0,500,80);
        //fontsize,leftright,topbutton,...,topbutton
        setLabel("First name",17,12,50,100,100);
        setLabel("Last name",17,12,115,100,100);
        setLabel("Email",17,12,190,100,100);
        setLabel("Username",17,304,50,100,100);
        setLabel("Password",17,304,120,100,100);
        setLabel("Mobile number",17,304,190,200,100);
        //add text fields. see method description for more details
        setTextField(100,90,130,20);
        setTextField(100,160,130,20);
        setTextField(100,230,130,20);
        setTextField(420,90,130,20);
        setTextField(420,160,130,20);
        setTextField(420,230,130,20);
        //buttons
        JButton registerBtn = new JButton("Register");
        //x, y coordinates, width, height
        registerBtn.setBounds(228,285,120,40);
        //add button with its set properties
        panel.add(registerBtn);
        //add panel with all its properties and components added 
        //inside it to the main frame
        frame.add(panel);
        //600 width 350 height
        //setPreferredSize was used instead of setSize
        
        panel.setPreferredSize(new Dimension(600,350));
        //set size of frame as per preferred size of components inside
        frame.pack();
        //terminate the program when app is closed
        //only hides the app by default
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        //show frame. hidden by default
        frame.setVisible(true);
    }

    
    private static void setLabel(String name, int fontSize, int...bounds){
        JLabel label = new JLabel(name);//create a label
        //set coordinates and sizes as per first 4 arguments to bounds
        label.setBounds(bounds[0],bounds[1],bounds[2],bounds[3]);
        //default font faimly and style, font size as per argument
        label.setFont(new Font(null, 0, fontSize));
        //add the created label to global panel component
        panel.add(label);
    }

    
    private static void setTextField(int...bounds){
        //create text field where user can write/fill data inside
        JTextField textField = new JTextField();
        //set coordinates and sizes as per first 4 arguments
        textField.setBounds(bounds[0],bounds[1],bounds[2],bounds[3]);
        //add the created text field component to global panel component
        panel.add(textField);
    }
}