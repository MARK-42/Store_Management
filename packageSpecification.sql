create or replace PACKAGE management IS

    FUNCTION get_hash (p_username  IN  VARCHAR2, p_password  IN  VARCHAR2) RETURN VARCHAR2;

    PROCEDURE insertEmployee (fn tabEmployee.firstName%type, ln tabEmployee.lastName%type, un tabEmployee.username%type, ps tabEmployee.password%type, pn tabEmployee.phoneNumber%type, ad tabEmployee.address%type, ema tabEmployee.email%type, sa tabEmployee.salary%type, ma tabEmployee.isManager%type, exitc OUT varchar2);

    PROCEDURE validEmployee (un tabEmployee.username%type, ps tabEmployee.password%type, exitc OUT varchar2);

    PROCEDURE insertCustomer (fn tabCustomer.firstName%type, ln tabCustomer.lastName%type, pn tabCustomer.phoneNumber%type, ad tabCustomer.address%type, em tabCustomer.email%type, ta tabCustomer.totalAmount%type, exitc OUT varchar2);

    PROCEDURE searchCustomerId (pn tabCustomer.phoneNumber%type, exitc OUT varchar2, result OUT tabCustomer.customerId%type);

    PROCEDURE checkStock (pId tabProductStock.productId%type, quant tabProductStock.totalQuantity%type, exitc OUT varchar2, result OUT boolean);

    PROCEDURE searchProductId (prn tabProductStock.productName%type, cat tabProductStock.catagory%type, exitc OUT varchar2, result OUT varchar2);

    PROCEDURE insertStock(id tabProductStock.productId%type, prn tabProductStock.productName%type, cat tabProductStock.catagory%type, quant tabProductStock.totalQuantity%type, pr tabProductStock.price%type, wei tabProductStock.weight%type, exitc OUT varchar2);

    PROCEDURE updateStockQuantity(pId tabProductStock.productId%type, quant tabProductStock.totalQuantity%type, exitc OUT varchar2);

    PROCEDURE insertRegister(p_id tabProductRegister.productId%type, b_id tabProductRegister.billId%type, quant tabProductRegister.quantity%type, sl_pr tabProductRegister.sellPrice%type, exitc OUT varchar2);

    PROCEDURE generateBill(c_id tabBill.customerId%type, cs_id tabBill.employeeId%type, amt tabBill.amount%type, ti tabBill.totalItems%type,p_m tabBill.paymentMethod%type,billTime tabBill.billTime%type,billDate tabBill.billDate%type,exitc OUT varchar2, result OUT number);

    PROCEDURE getAllProducts(result OUT varchar2);

END management;
/

commit;