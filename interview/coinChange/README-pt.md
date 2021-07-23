# Coin Change Problem in python
<br/>

## Motivo:
Muitas pessoas como eu, estão buscando uma vaga de emprego na área da tecnologia, mas muitas vezes nos esquecemos de treinar para possiveis entrevistas práticas.
Recentemente me deparei com a mesma situação, era um problema bem parecido com o que tentei resolver aqui.<br/>
O objetivo era contar quantas somas poderiam ser feitas para alcançar um determinado valor (12 no meu caso). Por estar mal acostumado a resolver problemas assim, tive muita
dificuldade para resolver e acredito que perdi a oportunidade, mas o que conta é o que aprendemos ao decorrer da jornada... então aqui estou eu para tentar ajudar quem quer que
esteja precisando de uma "explicação" para o problema.

## O problema:
O problema é bem simples, temos uma lista de valores/moedas de 25 cents, 10 cents, 5 cents e 1 cent... para facilitar vamos chama-la de **coins**, cada uma
dessas moedas deve ser somada até atingir um valor, que vamos chamar de goal, no nosso caso será chamada de **goal** e tera o valor 12.<br/>
É obrigatório criarmos um método chamado ***makeChange()*** que vai fazer a troca e exibir o resultado, podemos usar os **Sets**, um tipo de estrutura de dados para que repetições 
sejam evitadas, mas no código não utilizei, também pode-se criar outros métodos contanto que sua funcionalidade seja explicada em alguns comentários no próprio programa
