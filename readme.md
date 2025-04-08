Este projeto consiste no desenvolvimento de um sistema distribuído, baseado em arquitetura de microsserviços conteinerizados, voltado ao gerenciamento e recomendação de óleos essenciais. A proposta busca simular uma aplicação voltada para usuários que desejam utilizar óleos essenciais de forma segura e personalizada, de acordo com seus sintomas e características pessoais (como gestação ou condições de saúde).

A solução contará com quatro microsserviços principais, todos implementados em Python e empacotados em contêineres Docker, sendo consumidos por uma aplicação cliente em linha de comando. Cada serviço será responsável por uma única responsabilidade, seguindo os princípios da arquitetura de microsserviços:

Catálogo de Óleos Essenciais: apresenta a lista completa de óleos, com propriedades e benefícios.

Recomendações Personalizadas: sugere óleos com base nos sintomas informados pelo usuário.

Misturas e Favoritos: permite ao usuário salvar combinações personalizadas de óleos.

Contraindicações: verifica restrições com base no perfil do usuário, garantindo um uso seguro.

arquitetura proposta ainda poderá ser expandida no futuro com um front-end ou funcionalidades extras como histórico de uso. Essa solução explora práticas modernas de desenvolvimento distribuído e se baseia em um tema original, relevante e aplicável na vida real.

├── catalogo/ # Microsserviço 1 – Catálogo de óleos
├── recomendacoes/ # Microsserviço 2 – Recomendações por sintomas
├── misturas/ # Microsserviço 3 – Combinações favoritas
├── contraindicacoes/ # Microsserviço 4 – Verificação de contraindicações
├── cliente/ # Cliente (linha de comando)
├── docker-compose.yml # Arquivo para orquestrar os serviços
