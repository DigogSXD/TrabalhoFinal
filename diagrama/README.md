      
              Sistema         
                              
         cadastrar_aluno()    
         buscar_alunos()      
         registrar_matricula()
         cadastrar_missao()   
         registrar_participacao()
         gerar_relatorio_missoes()
         criar_equipe()       
         gerenciar_membros()  
         consultar_equipes()  
         menu()               
                        
        ^                   ^
        |                   |
        |                   |
        |                   |
        |                   |
        |                   |
         
  |    Admin  |       |  Instrutor |
         



         Aluno       
 nome            
 idade           
 habilidades     
 nivel_poder     
 equipe          
 status_matricula

  cadastrar()     
  buscar()        



        Missao      

 objetivo        
 equipe_designada
 data_inicio     
 data_termino    
 status          
 participantes   

  cadastrar()     
  registrar_participacao()
  gerar_relatorio()



       Equipe      

 nome            
 membros         
 instrutor       

  criar()         
  gerenciar_membros()
  consultar()     



       Aula        

 nome            
 instrutor       
 vagas           
 alunos_matriculados

  registrar_matricula()

