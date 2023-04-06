// Import IPFS library
const IPFS = require('ipfs-core')

// Define the main function
async function main() {
  // Create an IPFS node instance
  const node = await IPFS.create()

  // Upload file to the IPFS network
  const file = new Blob(['Hello, IPFS!'])
  const fileAdded = await node.add(file)

  // Log the file's CID to the console
  console.log('File added to IPFS:', fileAdded.cid.toString())

  // Download file from the IPFS network
  const fileBuffer = await node.cat(fileAdded.cid)

  // Log the downloaded file content to the console
  console.log('Downloaded file content:', fileBuffer.toString())

  // Stop the IPFS node instance
  await node.stop()
}

// Call the main function
main()
