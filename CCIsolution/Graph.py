#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is a Graph calss
# author Yongjun Chen

debug = False

class Graph(object):

	def __init__(self):
		self.neighbors = {}
		self.visited = {}
		self.dfs_order = []
		self.bfs_order = []
		self.queue = []

	def reset(self):
		self.visited = {}
		self.dfs_order = []
		self.bfs_order = []
		self.queue = []

	def nodes_in_graph(self):
		return self.neighbors.keys()

	def add_node(self,item):
		if item not in self.nodes_in_graph():
			self.neighbors[item] = []

	def add_node_lists(self,item_list):
		for node in item_list:
			self.add_node(node)

	def add_edge(self,edge):
		u,v = edge
		if (v not in self.neighbors[u]) and (u not in self.neighbors[v]):
			self.neighbors[u].append(v)
			if u != v:
				self.neighbors[v].append(u)

	def show_graph(self):
		print('nodes',list(self.neighbors))
		print('edges',list(self.neighbors.values()))

	def deep_first_search(self,node):
		self.visited[node] = True
		self.dfs_order.append(node)
		for n in self.neighbors[node]:
			if n not in self.visited:
				self.deep_first_search(n)

	def do_deep_first_search(self,root=None):
		if root:
			self.deep_first_search(root)
		else:
			for node in self.nodes_in_graph():
				self.deep_first_search(node)
		print("dfs result",self.dfs_order)
		self.reset()

	def bread_first_search(self):
		while len(self.queue) > 0:
			node = self.queue.pop(0)
			self.visited[node] = True
			for n in self.neighbors[node]:
				if (n not in self.visited) and (n not in self.queue):
					self.queue.append(n)
					self.bfs_order.append(n)

	def do_bread_first_search(self,root=None):
		if root:
			self.queue.append(root)
			self.bfs_order.append(root)
			self.bread_first_search()
		else:
			for n in self.nodes_in_graph():
				self.queue.append(n)
				self.bfs_order.append(n)
				self.bread_first_search()		
		print("bfs result",self.bfs_order)
		self.reset()

if __name__ == '__main__':
	a_graph= Graph()
	a_graph.add_node_lists(['a','b','c','d','e'])
	a_graph.add_edge(('a','b'))
	a_graph.add_edge(('a','c'))
	a_graph.add_edge(('b','d'))
	a_graph.add_edge(('b','e'))
	a_graph.do_deep_first_search('a')
	a_graph.do_bread_first_search('a')
	a_graph.show_graph()




