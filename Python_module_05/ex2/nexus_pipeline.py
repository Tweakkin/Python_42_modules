from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol

class ProcessingPipeline(ABC):
	pass


class base(Protocol):
	def build(self):
		pass


class builder:
	def build(self):
		print("Hello world!")

def testing(player: base):
	player.build()

def main() -> None:
	print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

if __name__ == "__main__":
	main()
	yahya = builder()
	testing(yahya)

