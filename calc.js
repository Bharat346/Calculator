document.addEventListener("DOMContentLoaded",()=>{
    console.log("calculator start.....")
    let y ;
    const btns = document.querySelectorAll('button')
    Array.from(btns).forEach(btn =>{
        //console.log(btn.textContent.trim())
        let btn2 = btn.textContent.trim();
        btn.addEventListener("click",(elem)=>{
            console.log(elem.target.textContent.trim());
            let char = elem.target.textContent.trim()
            if (char != '=' && char !='backspace') {
                document.getElementById('display').value += char;
            }
            if(char === 'C'){
                document.getElementById('display').value = "";
            }
            if(char === '='){
                var val = document.getElementById('display').value;
                console.log(val)
                if (val.includes("Σ")) {
                    val = val.replace("Σ","Sigma")
                }
                if (val.includes("d/dy")) {
                    val = val.replace("d/dy","Diff")
                }
                if (val.includes("∫")) {
                    val = val.replace("∫","Inte")
                }
                val = change_char(val)
                console.log(val)
                try {
                    
                    document.getElementById('display').value = eval(val);
                } catch (error) {
                    document.getElementById('display').value = "Error!! Incorrect Expression";
                    console.log(error)
                }
            }
        })
    })

    
    function change_char(str){
        str = str.replace(/\bsin\b/g, "Math.sin");
        str = str.replace(/\bcos\b/g, "Math.cos");
        str = str.replace(/\btan\b/g, "Math.tan");
        str = str.replace(/\barcsin\b/g, "Math.asin");
        str = str.replace(/\barccos\b/g, "Math.acos");
        str = str.replace(/\barctan\b/g, "Math.atan");
        str = str.replace(/\bpi\b/g, "Math.PI");
        str = str.replace(/\be\b/g, "Math.exp(1)");
        //str = str.replace(/\blog(${x})\b/g, `Math.log(${x},10)`);
        str = str.replace(/\bln\b/g,`Math.log`);
        
        if (str.includes("log")) {
            
            str = str.replace(/log\(([^]+)\)/g, `Math.log($1,10)`);
        }
        if (str.includes("^")) {
            str = str.replace(/(\w+)\s*\^\s*(\w+)/g, 'Math.pow($1, $2)');
        }
        if (str.includes("!")) {
            str = str.replace(/(\w+)\s*\!\s*/g,`factorial($1)`)
        }
        // if (str.includes("Σ")) {
        //     str = str.replace(/Σ/g, 'Sigma');
        // }
        return str;
    }

    function factorial(n) {
        if (n === 0 || n === 1) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }
    
    function Comb(n, r) {
        if (n < r) {
            return 0; // Invalid input, n should be greater than or equal to r
        }
        return factorial(n) / (factorial(r) * factorial(n - r));
    }

    function Perm(n, r) {
        if (n < r) {
            return 0; // Invalid input, n should be greater than or equal to r
        }
        return factorial(n) / factorial(n - r);
    }

    function Sigma(exp){
        let sum = 0;
        let l = Number.parseInt(document.getElementById("sigmaLimit1").value);
        let u = Number.parseInt(document.getElementById("sigmaLimit2").value);
        exp = document.getElementById("display").value;
        console.log(exp);
        exp = exp.replace("Σ","");
        
        exp = change_char(exp)
        console.log(exp);
        for ( let y = l; y <= u; y++) {
            sum += eval(exp,{y});
        }
        console.log(sum)
        return sum;
        
    }

    function Diff(exp){
        
        exp = document.getElementById("display").value;
        console.log(exp);
        exp = exp.replace("d/dy","");
        
        exp = change_char(exp)
        console.log(exp)
        const derivative = math.derivative(exp,'y')
        const result = derivative.toString();
        console.log(result);
        return result;
    }

    
    
    
})
