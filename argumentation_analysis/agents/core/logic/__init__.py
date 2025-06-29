# argumentation_analysis/agents/core/logic/__init__.py
"""
Package pour les agents de logique généralisés supportant différents types de logiques.

Ce package contient les implémentations des agents logiques pour différents types de logiques :
- Logique propositionnelle
- Logique du premier ordre
- Logique modale

Il fournit également une factory pour créer les agents appropriés et des utilitaires
pour gérer les ensembles de croyances et exécuter des requêtes logiques.
"""

from .propositional_logic_agent import PropositionalLogicAgent
from .fol_logic_agent import FOLLogicAgent
from .modal_logic_agent import ModalLogicAgent
from .logic_factory import LogicAgentFactory
from .belief_set import BeliefSet, PropositionalBeliefSet, FirstOrderBeliefSet, ModalBeliefSet
from .query_executor import QueryExecutor

__all__ = [
    'PropositionalLogicAgent',
    'FOLLogicAgent',
    'ModalLogicAgent',
    'LogicAgentFactory',
    'BeliefSet',
    'PropositionalBeliefSet',
    'FirstOrderBeliefSet',
    'ModalBeliefSet',
    'QueryExecutor'
]