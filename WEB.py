import Web3 from 'web3';

const web3 = new Web3(Web3.givenProvider || 'http://localhost:8545');
const contractAddress = 'YOUR_CONTRACT_ADDRESS';
const contractABI = 'YOUR_CONTRACT_ABI';
const contract = new web3.eth.Contract(contractABI, contractAddress);

async function createTopic(content) {
  const accounts = await web3.eth.getAccounts();
  await contract.methods.createTopic(content).send({ from: accounts[0] });
}

async function vote(topicId) {
  const accounts = await web3.eth.getAccounts();
  await contract.methods.vote(topicId).send({ from: accounts[0] });
}

async function getTopicRanking() {
  // Get topic count and fetch topic details one by one
  const topicCount = await contract.methods.topicCount().call();
  const topics = [];
  for (let i = 1; i <= topicCount; i++) {
    const topic = await contract.methods.getTopic(i).call();
    topics.push(topic);
  }

  // Sort topics by vote count
  topics.sort((a, b) => b.voteCount - a.voteCount);

  return topics;
}
