import java.util.Random;
public abstract class AccountHolder {
protected int ID;
protected String address;
	public AccountHolder(int ID, String address) {
		this.ID = ID;
		this.address = address;
	}
	public static int getNextID () {
		return new Random().nextInt(1000000);
	}
}
public class Account {
private AccountHolder holder;
private double balance = 0;
	public Account(double amount, AccountHolder holder) {
		this.holder = holder;
		this.balance = amount;
	}
	public void deposit(double amount) {
		balance = balance + amount;
	}
	public void withdraw(double amount) {
		balance = balance - amount;
	}
	public double getBalance() {
		return balance;
	}
	public AccountHolder getAccountHolder() {
		return holder;
	}
	public void setBalance(double amt) {
		balance = amt;
	}
	public void setHolder(AccountHolder holder) {
		this.holder = holder;
	}
}
public class IndividualHolder extends AccountHolder implements Util {
private String name;
private String SSN;
	public IndividualHolder(int ID, String address, String name, String SSN) {
		super(ID, address);
		this.name = name;
		this.SSN = SSN;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getSSN() {
		return SSN;
	}
	public void setSSN(String sSN) {
		SSN = sSN;
	}
	public String convertNameUpperCase(String name){
		return name.toUpperCase(); 
	}
}
interface Util {

	public String convertNameUpperCase(String name);

}
public class CorporateHolder extends AccountHolder {
private String contact;
	public CorporateHolder (int ID, String address, String contact) {
	super(ID, address);
	this.contact = contact;
	}
	public String getContact() {
		return contact;
	}
	public void setContact(String contact) {
		this.contact = contact;
	}
}
