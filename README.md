# ✉️ Gerador Automático de Cartas Personalizadas

Este projeto automatiza a criação de cartas personalizadas a partir de um **template** e de uma **lista de nomes**, gerando um ficheiro por destinatário na pasta final **ReadyToSend**.

---

## 📌 Objetivo

O objetivo deste projeto é facilitar a produção de múltiplas cartas personalizadas sem trabalho manual repetitivo.  
O utilizador fornece:

- Um ficheiro com nomes  
- Um template de carta contendo o placeholder `[name]`  

O programa gera automaticamente uma carta por pessoa.

---

## 🧠 Funcionamento

O processo segue quatro etapas principais:

1. **Criação automática das pastas**  
   O programa cria as pastas `Output/` e `Output/ReadyToSend/` caso ainda não existam.

2. **Leitura da lista de nomes**  
   Os nomes são carregados a partir de `invited_names.txt`, um por linha.

3. **Leitura do template da carta**  
   O ficheiro `starting_letter.txt` contém o texto base com o placeholder `[name]`.

4. **Geração das cartas personalizadas**  
   Para cada nome, o placeholder é substituído e é criado um ficheiro `letter_for_<nome>.txt`.

---

## 📝 Ficheiros de Entrada

### **invited_names.txt**
Lista de nomes, um por linha.

### **starting_letter.txt**
Template da carta contendo o placeholder `[name]`.

---

## ✔️ Exemplo de saída

```
letter_for_André.txt
letter_for_Hugo.txt
letter_for_Catarina.txt
...
```

Cada ficheiro contém o texto final com o nome substituído.