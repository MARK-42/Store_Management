create or replace PACKAGE BODY management AS

    FUNCTION get_hash (p_username  IN  VARCHAR2,
                     p_password  IN  VARCHAR2)
        RETURN VARCHAR2 AS
        l_salt VARCHAR2(30) := 'PutYourSaltHere';
    BEGIN
    -- Pre Oracle 10g
    --RETURN DBMS_OBFUSCATION_TOOLKIT.MD5(
    --  input_string => UPPER(p_username) || l_salt || UPPER(p_password));

    -- Oracle 10g+ : Requires EXECUTE on DBMS_CRYPTO
        RETURN DBMS_CRYPTO.HASH(UTL_RAW.CAST_TO_RAW(UPPER(p_username) || l_salt || UPPER(p_password)),DBMS_CRYPTO.HASH_SH1);
    END;

    PROCEDURE insertEmployee (fn tabEmployee.firstName%type, ln tabEmployee.lastName%type, un tabEmployee.username%type, ps tabEmployee.password%type, pn tabEmployee.phoneNumber%type, ad tabEmployee.address%type, ema tabEmployee.email%type, sa tabEmployee.salary%type, ma tabEmployee.isManager%type, exitc OUT varchar2) IS
    BEGIN
        INSERT INTO tabEmployee VALUES(employeeSeq.NEXTVAL, UPPER(fn), UPPER(ln), UPPER(un), get_hash(un,ps), pn, ad, UPPER(ema), sa, UPPER(ma));
        dbms_output.put_line('Operation was a success');
        exitc := 'Insert Success';
        COMMIT;
    EXCEPTION
        WHEN value_error THEN
            exitc := 'Insert failed';
        WHEN others THEN
            dbms_output.put_line('Error in inserting values');
            exitc := 'Insert failed';
    END;

    PROCEDURE validEmployee (un tabEmployee.username%type, ps tabEmployee.password%type, exitc OUT varchar2) IS
        v_dummy  VARCHAR2(1);
    BEGIN
        SELECT '1'
        INTO   v_dummy
        FROM   tabEmployee
        WHERE  username = UPPER(un)
        AND    password = get_hash(un, ps);
        exitc := 'Valid';
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
        exitc := 'Invalid';
        RAISE_APPLICATION_ERROR(-20000, 'Invalid username/password.');
    END;

    PROCEDURE insertCustomer (fn tabCustomer.firstName%type, ln tabCustomer.lastName%type, pn tabCustomer.phoneNumber%type, ad tabCustomer.address%type, em tabCustomer.email%type, ta tabCustomer.totalAmount%type, exitc OUT varchar2) IS
    BEGIN
        INSERT INTO tabCustomer VALUES(customerSeq.NEXTVAL, UPPER(fn), UPPER(ln), pn, ad, em, ta);
        dbms_output.put_line('Operation was a success');
        exitc := 'Insert Success';
        COMMIT;
    EXCEPTION
        WHEN value_error THEN
            exitc := 'Insert failed';
        WHEN others THEN
            dbms_output.put_line('Error in inserting values');
            exitc := 'Insert failed';
    END;

    PROCEDURE searchCustomerId (pn tabCustomer.phoneNumber%type, exitc OUT varchar2, result OUT tabCustomer.customerId%type) IS
    BEGIN
        SELECT customerId INTO result FROM tabCustomer WHERE phoneNumber = pn;
        exitc := 'Found';
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
        exitc := 'Not Found';
    END;

    PROCEDURE checkStock (pId tabProductStock.productId%type, quant tabProductStock.totalQuantity%type, exitc OUT varchar2, result OUT boolean) IS
        actualQuant tabProductStock.totalQuantity%type;
    BEGIN
        SELECT totalQuantity INTO actualQuant FROM tabProductStock WHERE productId = pId;
        IF quant <= actualQuant THEN
            result := TRUE;
            exitc := 'Available';
        ELSE
            result := FALSE;
            exitc := 'Only ' || actualQuant || ' available';
        END IF;
    END;

    PROCEDURE searchProductId (prn tabProductStock.productName%type, cat tabProductStock.catagory%type, exitc OUT varchar2, result OUT tabProductStock.productId%type) IS
    BEGIN
        SELECT productId INTO result FROM tabProductStock WHERE productName = UPPER(prn) AND catagory = UPPER(cat);
        exitc := 'Found';
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
        exitc := 'Not Found';
    END;

    PROCEDURE insertStock(id tabProductStock.productId%type, prn tabProductStock.productName%type, cat tabProductStock.catagory%type, quant tabProductStock.totalQuantity%type, pr tabProductStock.price%type, wei tabProductStock.weight%type, exitc OUT varchar2) IS
    BEGIN
        INSERT INTO tabProductStock VALUES(id,UPPER(prn),UPPER(cat),quant,pr,wei);
        dbms_output.put_line('Operation was a success');
        exitc := 'Insert Success';
        COMMIT;
    EXCEPTION
        WHEN value_error THEN
            exitc := 'Insert failed';
        WHEN others THEN
            dbms_output.put_line('Error in inserting values');
            exitc := 'Insert failed';
    END;

    PROCEDURE updateStockQuantity(pId tabProductStock.productId%type, quant tabProductStock.totalQuantity%type, exitc OUT varchar2) IS
        presentQuant tabProductStock.totalQuantity%type;
    BEGIN
        SELECT totalQuantity INTO presentQuant FROM tabProductStock WHERE productId = pId;
        UPDATE tabProductStock SET totalQuantity=presentQuant+quant WHERE productId=pId;
        exitc := 'Updated';
        COMMIT;
    EXCEPTION
        WHEN others THEN
            dbms_output.put_line('Error in updating value');
            exitc := 'Update failed';
    END;

    PROCEDURE insertRegister(p_id tabProductRegister.productId%type, b_id tabProductRegister.billId%type, quant tabProductRegister.quantity%type, sl_pr tabProductRegister.sellPrice%type, exitc OUT varchar2) IS
        presentQuant tabProductStock.totalQuantity%type;
    BEGIN
        SELECT totalQuantity INTO presentQuant FROM tabProductStock WHERE productId = p_id;
        INSERT INTO tabProductRegister VALUES(p_id,b_id,quant,sl_pr);
        UPDATE tabProductStock SET totalQuantity=presentQuant-quant WHERE productId=p_id;
        dbms_output.put_line('Operation was a success');
        exitc := 'Insert Success';
        COMMIT;
    EXCEPTION
        WHEN value_error THEN
            exitc := 'Insert failed';
        WHEN others THEN
            dbms_output.put_line('Error in inserting values');
            exitc := 'Insert failed';
    END;

    PROCEDURE generateBill(c_id tabBill.customerId%type, cs_id tabBill.employeeId%type, amt tabBill.amount%type, ti tabBill.totalItems%type,p_m tabBill.paymentMethod%type,billTime tabBill.billTime%type,billDate tabBill.billDate%type,exitc OUT varchar2, result OUT number) IS
        key tabBill.billId%type;
    BEGIN
        key := billSeq.NEXTVAL;
        INSERT INTO tabBill VALUES(key,c_id,cs_id,amt,ti,p_m,billTime,billDate);
        dbms_output.put_line('Operation was a success');
        result := key;
        exitc := 'Insert Success';
        COMMIT;
    EXCEPTION
        WHEN value_error THEN
            exitc := 'Insert failed';
        WHEN others THEN
            dbms_output.put_line('Error in inserting values');
            exitc := 'Insert failed';
    END;


    PROCEDURE getAllProducts(result OUT varchar2) IS
    CURSOR productsCursor IS SELECT productName,catagory FROM tabProductStock;
    BEGIN
        FOR i IN productsCursor
        LOOP
            result := result || ';' || i.productName || ',' || i.catagory;
        END LOOP;
    END;

END management;
/